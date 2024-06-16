from oauth2client.service_account import ServiceAccountCredentials
import gspread
import yaml

data = None
with open("higgingbotham.yaml") as file:
    lines = list(file)[1 : -1]
    data = yaml.safe_load("\n".join(lines))

if data is None:
    exit(1)

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "crucial-bonito-382823-5333eb85d775.json", scopes) # type: ignore

file = gspread.authorize(credentials)
sheet = file.open("Higgingbotham").sheet1

