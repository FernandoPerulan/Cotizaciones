from openbb import obb
import pandas as pd
import gspread
import json
from datetime import date

# ====== AUTENTICAR GOOGLE SHEETS ======
with open("credentials.json") as f:
    creds = json.load(f)
gc = gspread.service_account_from_dict(creds)
worksheet = gc.open("cotizaciones").sheet1

# ====== OBTENER COTIZACIONES ======
tickers = ["AAPL", "GOOGL", "MELI"]  # reemplazá por los que quieras
fecha_hoy = date.today().isoformat()

for ticker in tickers:
    df = obb.equity.price.historical(ticker, start_date="2025-08-01", end_date=fecha_hoy)
    # Último precio
    ultimo_precio = df.iloc[-1]["close"]
    
    # Escribir en Google Sheets
    worksheet.append_row([fecha_hoy, ticker, ultimo_precio])

print("Cotizaciones cargadas con éxito.")
