import dropbox
import os

DROPBOX_ACCESS_TOKEN = os.getenv("DROPBOX_ACCESS_TOKEN")

def subir_archivo(local_path, dropbox_path):
    if DROPBOX_ACCESS_TOKEN is None:
        raise ValueError("No se encontró la variable de entorno DROPBOX_ACCESS_TOKEN")
    dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    with open(local_path, "rb") as f:
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)
    print(f"Archivo subido a Dropbox en {dropbox_path}")
