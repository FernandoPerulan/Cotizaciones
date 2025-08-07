import yfinance as yf
import json

df = yf.download("AAPL", start="2024-01-01", end="2024-08-01")
df.reset_index(inplace=True)

# Elegimos algunas columnas útiles
df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]

# Convertimos las fechas a string (por compatibilidad)
df["Date"] = df["Date"].astype(str)

# Lo convertimos a lista de listas
data = df.values.tolist()

# Guardamos en JSON para pasárselo al step siguiente
with open("datos.json", "w") as f:
    json.dump(data, f)
