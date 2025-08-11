# main.py
from cotizaciones import crear_csv_cotizaciones
from dropbox_utils import subir_archivo

if __name__ == "__main__":
    # --- Configuración: editá según necesites ---
    tickers = ["AAPL", "MSFT", "GOOGL"]        # lista de tickers
    fecha_inicio = "01-07-2024"               # dd-mm-aaaa
    archivo_local = "cotizaciones.csv"
    dropbox_path = f"/inspirare/cotizaciones/{archivo_local}"
    # -------------------------------------------

    # Crear CSV
    crear_csv_cotizaciones(archivo_local, tickers, fecha_inicio)

    # Subir a Dropbox
    subir_archivo(archivo_local, dropbox_path)
    print("Proceso finalizado.")

