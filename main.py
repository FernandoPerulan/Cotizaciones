import dropbox
import os
import csv

DROPBOX_ACCESS_TOKEN = os.getenv("DROPBOX_ACCESS_TOKEN")
DROPBOX_PATH = "/inspirare/cotizaciones/archivo.csv"  # ruta completa en Dropbox

def crear_archivo_prueba(nombre_archivo):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Edad", "Ciudad"])
        writer.writerow(["Fernando", 30, "Mendoza"])
        writer.writerow(["Ana", 25, "Buenos Aires"])
    print(f"Archivo de prueba '{nombre_archivo}' creado.")

def subir_archivo(local_path):
    if DROPBOX_ACCESS_TOKEN is None:
        raise ValueError("No se encontró la variable de entorno DROPBOX_ACCESS_TOKEN")
    dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    with open(local_path, "rb") as f:
        dbx.files_upload(f.read(), DROPBOX_PATH, mode=dropbox.files.WriteMode.overwrite)
    print(f"Archivo subido a Dropbox en {DROPBOX_PATH}")

if __name__ == "__main__":
    archivo_local = "archivo.csv"
    crear_archivo_prueba(archivo_local)
    subir_archivo(archivo_local)
