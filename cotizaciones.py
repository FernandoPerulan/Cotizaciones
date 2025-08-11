import yfinance as yf
import csv
from datetime import datetime, timedelta

def obtener_cotizaciones(ticker, dias=5):
    fin = datetime.today()
    inicio = fin - timedelta(days=dias)
    data = yf.download(
        ticker, 
        start=inicio.strftime("%Y-%m-%d"), 
        end=fin.strftime("%Y-%m-%d")
    )
    return data['Close']  # Solo columna de cierre

def crear_csv_cotizaciones(nombre_archivo, tickers, dias):
    
    # Obtener datos para cada ticker
    precios_por_ticker = {}
    fechas_set = set()

    for ticker in tickers:
        data = obtener_cotizaciones(ticker, dias)
        precios_por_ticker[ticker] = data
        fechas_set.update(data.index)

    # Ordenar fechas más recientes primero
    fechas_ordenadas = sorted(fechas_set, reverse=True)

    # Crear archivo CSV
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Encabezado
        writer.writerow(["Fecha"] + tickers)

        for fecha in fechas_ordenadas:
            fila = [fecha.strftime("%d-%m-%Y")]
            for ticker in tickers:
                valor = precios_por_ticker[ticker].get(fecha, "")
                fila.append(round(valor, 2) if valor == valor else "")  # Evita NaN
            writer.writerow(fila)

