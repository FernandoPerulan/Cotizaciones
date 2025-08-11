# cotizaciones.py
# cotizaciones.py
import yfinance as yf
import pandas as pd
from datetime import datetime
import csv

def _serie_cierre(ticker, fecha_inicio):
    """
    Devuelve una Series (index datetime) de cierres diarios para ticker desde fecha_inicio hasta hoy.
    fecha_inicio: 'dd-mm-aaaa'
    """
    inicio_dt = datetime.strptime(fecha_inicio, "%d-%m-%Y")
    start = inicio_dt.strftime("%Y-%m-%d")
    # Descargar solo el ticker (evitamos MultiIndex)
    df = yf.download(ticker, start=start, end=None, progress=False, auto_adjust=False)
    if df is None or df.empty:
        return pd.Series(dtype='float64')
    # asegurarnos que índice sea datetime y ordenar
    df.index = pd.to_datetime(df.index)
    serie = df["Close"].astype(float).round(2)
    return serie

def crear_csv_cotizaciones(nombre_archivo, tickers, fecha_inicio):
    """
    Genera un CSV con:
    Fecha (dd-mm-aaaa), TICKER1, TICKER2, ...
    donde cada celda es el precio de cierre (round 2) o vacío si no hay dato.
    """
    # Diccionario de series por ticker
    series = {}
    for t in tickers:
        print(f"Descargando {t} desde {fecha_inicio} ...")
        s = _serie_cierre(t, fecha_inicio)
        series[t] = s

    # Unir en DataFrame por índice de fecha (outer join)
    if not series:
        raise ValueError("No se recibieron tickers")
    df = pd.DataFrame(series)

    # Convertir índice a formato dd-mm-aaaa y mover a columna
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()  # fechas ascendente (antiguas -> recientes); ajustá si querés inverso
    df.index = df.index.strftime("%d-%m-%Y")
    df.reset_index(inplace=True)
    df.rename(columns={"index": "Fecha"}, inplace=True)

    # Reemplazar NaN por cadena vacía (para CSV)
    df = df.where(pd.notna(df), "")

    # Guardar CSV con encabezado: Fecha, tickers...
    df.to_csv(nombre_archivo, index=False, encoding="utf-8", float_format="%.2f")
    print(f"CSV creado: {nombre_archivo} (filas: {len(df)})")
