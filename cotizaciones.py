# cotizaciones.py
import yfinance as yf
import csv
from datetime import datetime, timedelta

def obtener_cotizaciones(tickers, fecha_inicio, fecha_fin):
    # Descargar cotizaciones con yfinance
    data = yf.download(tickers, start=fecha_inicio, end=fecha_fin, group_by='ticker', auto_adjust=False)

    # Preparar diccionario con fechas y precios de cierre
    datos_por_fecha = {}

    # yfinance devuelve diferente formato si es un solo ticker o varios
    # Aseguramos que tickers sea lista
    if isinstance(tickers, str):
        tickers = [tickers]

    for ticker in tickers:
        # Para un solo ticker, data tiene columnas directas
        # Para varios tickers, data[ticker] contiene las columnas

        if len(tickers) == 1:
            df = data
        else:
            df = data[ticker]

        for fecha, fila in df.iterrows():
            fecha_str = fecha.strftime("%d-%m-%Y")
            if fecha_str not in datos_por_fecha:
                datos_por_fecha[fecha_str] = {}
            cierre = fila.get("Close", None)
            datos_por_fecha[fecha_str][ticker] = round(cierre, 2) if cierre == cierre else ""

    return datos_por_fecha

def guardar_csv(nombre_archivo, datos, tickers):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Fecha"] + tickers)
        for fecha in sorted(datos.keys(), key=lambda x: datetime.strptime(x, "%d-%m-%Y")):
            fila = [fecha]
            for ticker in tickers:
                fila.append(datos[fecha].get(ticker, ""))
            writer.writerow(fila)
