from cotizaciones import crear_csv_cotizaciones
from dropbox_utils import subir_archivo

if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOGL"]
    dias = 5

    archivo_local = "cotizaciones.csv"
    
    crear_csv_cotizaciones(archivo_local, tickers, dias)

    # Si querés subir a Dropbox
    dropbox_path = f"/inspirare/cotizaciones/{archivo_local}"
    subir_archivo(archivo_local, dropbox_path)