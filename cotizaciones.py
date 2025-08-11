import yfinance as yf
import csv
from datetime import datetime, timedelta

def obtener_cotizaciones(ticker, dias=5):
    fin = datetime.today()
    inicio = fin - timedelta(days=dias)
    data = yf.download(
        ticker,
        start=inicio.strftime("%Y-%m-%d"),
        end=fin.strftime("%Y-%m-%d"),
        auto_adjust=False
    )
    return data

def crear_csv_cotizaciones(nombre_archivo, tickers, dias=5):
    # Diccionario: {fecha: {ticker: precio_cierre}}
    datos_por_fecha = {}

    for ticker in tickers:
        data = obtener_cotizaciones(ticker, dias)
        for fecha, fila in data.iterrows():
            fecha_str = fecha.strftime("%d-%m-%Y")
            cierre = fila.get("Close", None)  # Evita error si no existe
            if fecha_str not in datos_por_fecha:
                datos_por_fecha[fecha_str] = {}
            datos_por_fecha[fecha_str][ticker] = round(cierre, 2) if cierre == cierre else ""

    # Guardar en CSV
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Encabezados
        writer.writerow(["Fecha"] + tickers)
        # Filas ordenadas por fecha
        for fecha in sorted(datos_por_fecha.keys(), key=lambda x: datetime.strptime(x, "%d-%m-%Y")):
            fila = [fecha]
            for ticker in tickers:
                fila.append(datos_por_fecha[fecha].get(ticker, ""))
            writer.writerow(fila)
