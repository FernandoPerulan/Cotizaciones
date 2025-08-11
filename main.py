from cotizaciones import crear_csv_cotizaciones
from dropbox_utils import subir_archivo

if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOGL"]
    fecha_inicio = "01-07-2024"  # Formato dd-mm-aaaa

    archivo_local = "cotizaciones.csv"
    
    # Crear el CSV con cotizaciones desde fecha_inicio hasta hoy
    crear_csv_cotizaciones(archivo_local, tickers, fecha_inicio)

    # Ruta en Dropbox donde subir el archivo
    dropbox_path = f"/inspirare/cotizaciones/{archivo_local}"
    
    # Subir archivo a Dropbox
    subir_archivo(archivo_local, dropbox_path)

    print(f"Archivo '{archivo_local}' creado y subido a Dropbox en '{dropbox_path}'.")
