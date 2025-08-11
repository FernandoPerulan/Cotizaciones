import json
with open("credentials.json") as f:
    creds = json.load(f)
print(creds)
