import os
import io
from httplib2 import Http
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from oauth2client.service_account import ServiceAccountCredentials
from pathlib import Path


SCOPES = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file']

creds = ServiceAccountCredentials.from_json_keyfile_name("../ingsoft_key.json", SCOPES)

file_ids = ['1mEHk8DJ3akqxJ0EUdpkClVVbP3I0lUiw','1fA8HtztfTW7oDFD8nUNlZ9PS2ORw0HLi']
file_names = ['PL - CTR N°476 Luke.pdf','PL - CTR N°475 Luke.pdf']

drive = build('drive', 'v3', http=creds.authorize(Http()))

for file_id, file_name in zip(file_ids, file_names):
    request = drive.files().get_media(fileId=file_id)

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)

    done = False
    
    while not done:
        status, done= downloader.next_chunk()
        print('Download progress {0}'.format(status.progress() * 100))
    
    fh.seek(0)

    with open(os.path.join('./Descargas', file_name), 'wb') as f:
        f.write(fh.read())
        f.close()
