import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPE)

client = gspread.authorize(creds)
sheet = client.open('test_sheet')

sheet_instance = sheet.get_worksheet(0)

def push_data(device_id, uid, uid_text=None, status=False):
    data = [str(datetime.now()), device_id, uid, uid_text, status]
    sheet_instance.append_row(data)
    # print("[+] Append ", data)
    last_entry = sheet_instance.get_all_records()[-1]
    return last_entry