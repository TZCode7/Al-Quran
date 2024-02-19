#!/usr/etc/env python3
import os
import sys
import json
import datetime
import requests
from rich import print
from rich.panel import Panel

os.system("clear")

def cari():
    url = "https://equran.id/api/v2/surat"
    respone = requests.get(url)
    if respone.status_code == 200:
        datas = json.loads(respone.text)
        data = datas['data']

        for dat in data:
            nomor = dat['nomor']
            nama = dat['nama']
            nama_Latin = dat['namaLatin']
            jumlah_ayat = dat['jumlahAyat']
            tempat_turun = dat['tempatTurun']
            arti = dat['arti']
            audio_full = dat['audioFull']
            print(Panel(f"[bold yellow]No : [bold white]{nomor}\nNama : {nama}\nNama_Latin : {nama_Latin}\njumlah_Ayat : {jumlah_ayat}\ntempat_Turun : {tempat_turun}\nArti : {arti}",title=f"{nomor}"))

def quran():
    cari()
    no = int(input("=> Choice : "))
    url_1 = f"https://equran.id/api/v2/surat/{no}"
    respone_url = requests.get(url_1)

    if respone_url.status_code == 200:
        data_1 = json.loads(respone_url.text)

        code = data_1['code']
        massage = data_1['message']
        data_ayat = data_1['data']
        ayat = data_ayat['ayat']
        for dara in ayat:
            nomorAyat = dara['nomorAyat']
            textArab = dara['teksArab']
            textLatin = dara['teksLatin']
            textIndonesia = dara['teksIndonesia']
            print(Panel(f"Nomor_Ayat : {nomorAyat}\nText_Arab : {textArab}\nText_Latin : {textLatin}\nText_Indonesia : {textIndonesia}",title=f"{nomorAyat}"))
quran()
