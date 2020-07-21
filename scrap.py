from bs4 import BeautifulSoup #mengimport package beautifulsoup4
import request #mengimport package request
from pip._vendor import requests
import menu_depan

# Membuat fungsi pencarian list kode kota



def CariDataKota():
    # memasukan url web yang akan di scrapping
    url = 'https://jadwalsholat.pkpu.or.id/monthly.php?id=274'

    # membuat variable contents yang mana berisi package perintah request
    # perintah request ditambah .get(url) berisi variable yang berisi url web
    contents = requests.get(url)

    # membuat variable soup, yang berisi perintah dari package bs4,
    # dimana isi variablenya berisi contents, & fungsi parsing html, untuk membuang tag HTML
    soup = BeautifulSoup(contents.text, "html.parser")

    # Mengambil halaman web bagian dropdown menu (option) serta nilai valuenya sebagai kode kota
    options = soup.select('select[name="kota"] option')
    # Melakukan looping variabel op, untuk menampilkan isi variabel options
    for op in options:
        # membuat variabel kode_kota yang berisikan variabel op dengan isi value(kode kota)
        kode_kota = op['value']
        # membuat variabel nama_kota yang berisikan variabel op dengan perintah get_text() untuk mengambil text
        nama_kota = op.get_text()
        # mencetak isi variabel kode_kota dan nama_kota berdampingan
        print(f'{kode_kota} | {nama_kota}')


#membuat fungsi cari waktu sholat
def CariWaktuSholat():
    # memasukan url web yang akan di scrapping
    # url = f'https://jadwalsholat.pkpu.or.id/monthly.php?id={inputkota}'

    # membuat variable contents yang mana berisi package perintah request
    # perintah request ditambah .get(url) berisi variable yang berisi url web
    contents = requests.get(url)
    response = BeautifulSoup(contents.text, "html.parser")
    data = response.find_all('tr', 'table_highlight')
    data = data[0]

    sholat = {}
    i = 0
    for d in data:
        if  i == 1:
            sholat['subuh'] = d.get_text()
        elif i == 2:
            sholat['zuhur'] = d.get_text()
        elif i == 3:
            sholat['ashar'] = d.get_text()
        elif i == 4:
            sholat['maghrib'] = d.get_text()
        elif i == 5:
            sholat['isya'] = d.get_text()
        i += 1

    print(f'\nsholat')
