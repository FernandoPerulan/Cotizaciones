# cotizaciones.py
import yfinance as yf
from openbb import obb
import csv
from datetime import datetime

def obtener_cotizaciones_yf(ticker, fecha_inicio):
    inicio = datetime.strptime(fecha_inicio, "%d-%m-%Y")
    data = yf.download(
        ticker,
        start=inicio.strftime("%Y-%m-%d"),
        auto_adjust=False
    )
    return data

def obtener_cotizaciones_openbb(ticker, fecha_inicio):
    # Convertir la fecha de dd-mm-aaaa a YYYY-MM-DD
    inicio = datetime.strptime(fecha_inicio, "%d-%m-%Y").strftime("%Y-%m-%d")
    # Llamar a la API nueva de OpenBB para precios históricos
    data = obb.equity.price.historical(
        symbol=ticker,
        start_date=inicio
    )
    # Devuelve un DataFrame de pandas con las cotizaciones
    return data.to_df()

def crear_csv_cotizaciones(nombre_archivo, tickers, fecha_inicio):
    datos_por_fecha = {}

    for ticker in tickers:
        # YFinance
        data_yf = obtener_cotizaciones_yf(ticker, fecha_inicio)
        for fecha, fila in data_yf.iterrows():
            fecha_str = fecha.strftime("%d-%m-%Y")
            if fecha_str not in datos_por_fecha:
                datos_por_fecha[fecha_str] = {}
            cierre_yf = fila.get("Close", None)
            datos_por_fecha[fecha_str][f"{ticker}_YF"] = round(cierre_yf, 2) if cierre_yf == cierre_yf else ""

        # OpenBB
        data_obb = obtener_cotizaciones_openbb(ticker, fecha_inicio)
        if not data_obb.empty:
            for fecha, fila in data_obb.iterrows():
                fecha_str = fecha.strftime("%d-%m-%Y")
                if fecha_str not in datos_por_fecha:
                    datos_por_fecha[fecha_str] = {}
                cierre_obb = fila.get("Close", None)
                datos_por_fecha[fecha_str][f"{ticker}_OBB"] = round(cierre_obb, 2) if cierre_obb == cierre_obb else ""

    # Guardar CSV
    columnas = ["Fecha"] + [f"{t}_YF" for t in tickers] + [f"{t}_OBB" for t in tickers]
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(columnas)

        for fecha in sorted(datos_por_fecha.keys(), key=lambda x: datetime.strptime(x, "%d-%m-%Y")):
            fila = [fecha]
            for col in columnas[1:]:
                fila.append(datos_por_fecha[fecha].get(col, ""))
            writer.writerow(fila)
