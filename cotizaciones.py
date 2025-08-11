# cotizaciones.py
import yfinance as yf
import pandas as pd
from datetime import datetime
import csv

def _serie_cierre(ticker, fecha_inicio):
    """
    Devuelve una Series (index datetime) con cierres diarios para ticker desde fecha_inicio hasta hoy.
    fecha_inicio: 'dd-mm-aaaa'
    """
    inicio_dt = datetime.strptime(fecha_inicio, "%d-%m-%Y")
    start = inicio_dt.strftime("%Y-%m-%d")
    df = yf.download(ticker, start=start, end=None, progress=False, auto_adjust=False)
    if df is None or df.empty:
        return pd.Series(dtype='float64')
    s = df["Close"].astype(float).round(2)
    s.index = pd.to_datetime(s.index)
    return s

def crear_csv_cotizaciones(nombre_archivo, tickers, fecha_inicio):
    """
    Genera CSV con columnas: Fecha (dd-mm-aaaa), TICKER1, TICKER2, ...
    """
    series_dict = {}
    for t in tickers:
        print(f"Descargando {t} desde {fecha_inicio} ...")
        s = _serie_cierre(t, fecha_inicio)
        if not s.empty:
            # aseguramos que la Series tenga el nombre del ticker
            s.name = t
            series_dict[t] = s
        else:
            print(f"  -> No hay datos para {t} en el rango pedido.")

    if series_dict:
        # concat dict of series -> DataFrame with columns = tickers
        df = pd.concat(series_dict, axis=1)
        # ordenar por fecha ascendente y formatear índice
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        df.index = df.index.strftime("%d-%m-%Y")
        df.reset_index(inplace=True)
        df.rename(columns={"index": "Fecha"}, inplace=True)
        # rellenar NaN con cadena vacía
        df = df.where(pd.notna(df), "")
    else:
        # si no hay series con datos, crear DataFrame vacío con header
        cols = ["Fecha"] + tickers
        df = pd.DataFrame(columns=cols)

    # Guardar CSV (float_format no forzamos porque convertimos NaN a "")
    df.to_csv(nombre_archivo, index=False, encoding="utf-8")
    print(f"CSV creado: {nombre_archivo} (filas: {len(df)})")
