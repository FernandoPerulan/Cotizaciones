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
    # Diccionario para almacenar todas las cotizaciones por fecha
    cotizaciones_por_fecha = {}

    for ticker in tickers:
        data = obtener_cotizaciones(ticker, dias)
        for fecha, fila in data.iterrows():
            fecha_str = fecha.strftime("%d-%m-%Y")
            cierre = fila['Close']
            if fecha_str not in cotizaciones_por_fecha:
                cotizaciones_por_fecha[fecha_str] = {}
            cotizaciones_por_fecha[fecha_str][ticker] = cierre

    # Ordenamos las fechas
    fechas_ordenadas = sorted(
        cotizaciones_por_fecha.keys(),
        key=lambda x: datetime.strptime(x, "%d-%m-%Y")
    )

    # Escribir CSV
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        encabezado = ["Fecha"] + tickers
        writer.writerow(encabezado)

        for fecha_str in fechas_ordenadas:
            fila = [fecha_str]
            for ticker in tickers:
                valor = cotizaciones_por_fecha[fecha_str].get(ticker, "")
                if isinstance(valor, (int, float)):  # Solo redondear si es número
                    fila.append(round(valor, 2))
                else:
                    fila.append("")
            writer.writerow(fila)

