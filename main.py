import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Mostrar contenido de credentials.json para debug
try:
    with open("credentials.json", "r") as f:
        content = f.read()
    print("Contenido de credentials.json:\n", content)
except Exception as e:
    print(f"Error al leer credentials.json: {e}")
    exit(1)

# Configurar permisos requeridos por Sheets API
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

try:
    # Leer credenciales del archivo JSON
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
except Exception as e:
    print(f"Error al autenticar con Google Sheets: {e}")
    exit(1)

try:
    # Abrir la hoja por ID
    spreadsheet = client.open_by_key("1AfkLPUEPebyr5HP99f8BMuhzblME5WSN_kuf4kzM7t0")
    worksheet = spreadsheet.worksheet("Hoja1")
    
    # Leer las primeras 5 filas para verificar conexión
    rows = worksheet.get_all_values()[:5]
    print("Primeras filas de la hoja:")
    for row in rows:
        print(row)
except Exception as e:
    print(f"Error al acceder o leer la hoja: {e}")
    exit(1)

print("Autenticación y lectura exitosas.")
