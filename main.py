import gspread
import json

# Leer archivo de credenciales
with open("credentials.json") as f:
    creds = json.load(f)

# Autenticarse con gspread
gc = gspread.service_account_from_dict(creds)

# Abrir la hoja de cálculo (poné el nombre exacto)
spreadsheet = gc.open("cotizaciones")

# Seleccionar la primera hoja
worksheet = spreadsheet.sheet1

# Datos para agregar (ejemplo)
fila = ["Fernando", "Probando escritura", "2025-08-07"]

# Agregar fila al final
worksheet.append_row(fila)

print("Fila agregada con éxito.")
