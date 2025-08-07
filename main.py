import gspread
import json

# Leer el archivo de credenciales
with open("credentials.json") as f:
    creds = json.load(f)

# Autenticarse con gspread
gc = gspread.service_account_from_dict(creds)

# Abrir la hoja de cálculo por nombre (asegurate que sea el correcto)
spreadsheet = gc.open("cotizaciones")  # Reemplazá con el nombre exacto

# Seleccionar la primera pestaña (worksheet)
worksheet = spreadsheet.sheet1

# Fila de datos para escribir
fila = ["Fernando", "Probando escritura", "2025-08-07"]

# Agregar la fila al final de la hoja
worksheet.append_row(fila)

print("Fila agregada con éxito.")
