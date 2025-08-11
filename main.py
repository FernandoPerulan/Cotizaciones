from cotizaciones import obtener_cotizaciones, crear_csv_cotizaciones
from dropbox_utils import subir_archivo

if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOGL"]
    dias = 5

    for ticker in tickers:
        archivo_local = f"{ticker}_cotizaciones.csv"
        dropbox_path = f"/inspirare/cotizaciones/{archivo_local}"

        data = obtener_cotizaciones(ticker, dias)
        crear_csv_cotizaciones(archivo_local, data)
        subir_archivo(archivo_local, dropbox_path)
