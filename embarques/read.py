import gspread
from oauth2client.service_account import ServiceAccountCredentials


SERVICE_ACCOUNT_FILE = 'ingsoft_key.json'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = ServiceAccountCredentials.from_json_keyfile_name("../ingsoft_key.json", SCOPES)

client = gspread.authorize(creds)

spreadsheet = client.open("Maestro de Importaciones").worksheet("Data to App")
requested_data = spreadsheet.get_all_records()



# The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1ag4Rii1MB2mwuv7LqebQNFR-GvlfQQ9DmHg6qt7TIiM'


# service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
# sheet = service.spreadsheets()
# result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                             range="'Data to App'!A1:J15").execute()


# values = result.get_all_records()





