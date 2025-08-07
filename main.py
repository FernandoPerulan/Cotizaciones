import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configurar permisos requeridos por Sheets API
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

# Leer credenciales del archivo JSON
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Abrir la hoja por ID y seleccionar la hoja por nombre
spreadsheet = client.open_by_key("1AfkLPUEPebyr5HP99f8BMuhzblME5WSN_kuf4kzM7t0")  #  Reemplaza con el ID real
worksheet = spreadsheet.worksheet("Hoja1")         #  Reemplaza con el nombre real

# Datos a insertar
data = [
    ["Nombre", "Edad", "Ciudad"],
    ["Ana", 25, "Mendoza"],
    ["Juan", 30, "San Rafael"]
]

# Agregar filas
worksheet.append_rows(data)
print("Datos escritos en Google Sheets.")
