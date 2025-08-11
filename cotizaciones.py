import yfinance as yf
import csv
from datetime import datetime, timedelta

def obtener_cotizaciones(ticker, dias=5):
    fin = datetime.today()
    inicio = fin - timedelta(days=dias)
    data = yf.download(ticker, start=inicio.strftime("%Y-%m-%d"), end=fin.strftime("%Y-%m-%d"))
    return data

def crear_csv_cotizaciones(nombre_archivo, data):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Fecha", "Apertura", "Maximo", "Minimo", "Cierre", "Volumen"])
        for fecha, fila in data.iterrows():
            writer.writerow([fecha.strftime("%Y-%m-%d"), fila['Open'], fila['High'], fila['Low'], fila['Close'], fila['Volume']])
