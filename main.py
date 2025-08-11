# main.py
from cotizaciones import crear_csv_cotizaciones
from dropbox_utils import subir_archivo

if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOGL"]
    fecha_inicio = "01-07-2024"  # dd-mm-aaaa

    archivo_local = "cotizaciones.csv"
    
    crear_csv_cotizaciones(archivo_local, tickers, fecha_inicio)

    # Subir a Dropbox
    dropbox_path = f"/inspirare/cotizaciones/{archivo_local}"
    subir_archivo(archivo_local, dropbox_path)
