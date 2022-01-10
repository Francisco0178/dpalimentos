from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Embarque
from django.contrib.auth.decorators import login_required

import os
import io
from httplib2 import Http
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

from pathlib import Path


import gspread
from oauth2client.service_account import ServiceAccountCredentials

SERVICE_ACCOUNT_FILE = 'ingsoft_key.json'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file']

creds = None
creds = ServiceAccountCredentials.from_json_keyfile_name("ingsoft_key.json", SCOPES)

client = gspread.authorize(creds)

spreadsheet = client.open("Maestro de Importaciones").worksheet("Data to App")
# requested_data = spreadsheet.get_all_records()
# lista_embarques = json.loads(requested_data)

# Create your views here.

requested_data = spreadsheet.get_all_records()

@login_required
def home(request):
    context = {
        'embarques': requested_data,
        'title': 'Home'
    }
    return render(request, 'embarques/home.html', context)

@login_required
def about(request):
    return render(request, 'embarques/about.html', {'title': 'About'})

@login_required
def historial(request):
    context = {
        'embarques': requested_data,
        'title': 'Historial'
    }
    return render(request, 'embarques/historial.html', context)

@login_required
def perfil(request):
    return render(request, 'embarques/perfil.html', {'title': 'Perfil'})

@login_required
def embarque(request):
    idUrl = request.GET.get('id')
    id = int(idUrl)

    for embarque in requested_data:
        if embarque['id'] == id:
            status = embarque['status']
            proveedor = embarque['proveedor']
            ctr = embarque['ctr']
            carga = embarque['carga']
            tipo = embarque['tipo']
            eta = embarque['eta']
            retiro = embarque['retiro']
            hora = embarque['hora']
            siglaCtr = embarque['siglaCtr']
            idPl = embarque['idPl']
            print(type(embarque['cantidad']))

    context = {
        'embarques' : requested_data,
        'id' : id,
        'status' : status,
        'proveedor' : proveedor,
        'ctr' : ctr,
        'carga': carga,
        'tipo': tipo,
        'eta': eta,
        'retiro': retiro,
        'hora': hora,
        'siglaCtr': siglaCtr,
        'idPl': idPl,
        'title': 'Embarque'
    }
    return render(request, 'embarques/embarque.html', context)


@login_required
def runCode(request):

    idUrl = request.GET.get('id')
    id = int(idUrl)

    for embarque in requested_data:
        if embarque['id'] == id:
            file_id = embarque['idPl']
            file_name = embarque['nombrePl']

    drive = build('drive', 'v3', http=creds.authorize(Http()))

    request = drive.files().get_media(fileId=file_id)

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)

    done = False
    
    while not done:
        status, done= downloader.next_chunk()
        print('Download progress {0}'.format(status.progress() * 100))
    
    fh.seek(0)
    
    downloads_path = "../downloads"


    with open(os.path.join(downloads_path, file_name), 'wb') as f:
        f.write(fh.read())
        f.close()
    
    resp = HttpResponse(fh.getvalue(), content_type="application/pdf")
    
    resp['Content-Disposition'] = 'attachment; filename="%s"' % file_name

    return resp

    