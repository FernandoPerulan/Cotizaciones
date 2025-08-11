import dropbox
import os
import csv
import yfinance as yf
from datetime import datetime, timedelta

DROPBOX_ACCESS_TOKEN = os.getenv("DROPBOX_ACCESS_TOKEN")
DROPBOX_PATH = "/inspirare/cotizaciones/cotizaciones.csv"  # ruta en Dropbox para cotizaciones

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
    print(f"Archivo de cotizaciones '{nombre_archivo}' creado.")

def subir_archivo(local_path):
    if DROPBOX_ACCESS_TOKEN is None:
        raise ValueError("No se encontró la variable de entorno DROPBOX_ACCESS_TOKEN")
    dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    with open(local_path, "rb") as f:
        dbx.files_upload(f.read(), DROPBOX_PATH, mode=dropbox.files.WriteMode.overwrite)
    print(f"Archivo subido a Dropbox en {DROPBOX_PATH}")

if __name__ == "__main__":
    ticker = "AAPL"  # Cambia por el ticker que quieras
    archivo_local = "cotizaciones.csv"
    data = obtener_cotizaciones(ticker)
    crear_csv_cotizaciones(archivo_local, data)
    subir_archivo(archivo_local)
