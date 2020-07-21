import scrap
from bs4 import BeautifulSoup #mengimport package beautifulsoup4
import request #mengimport package request
from pip._vendor import requests

def MenuDepan():
    print('\n###################################################')
    print('#_________Program Cek Jadwal Sholat_______________#')
    print('#__By : Muhammad Shofyan <shofyankhan@gmail.com>__#')
    print('#_Sumber Data : https://jadwalsholat.pkpu.or.id/ _#')
    print('###################################################')

    print('\nPilih Menu yang anda inginkan :')
    print('1. Lihat Kode Kota')
    print('2. Masukan Kota Anda')

    MenuAwal = int(input("\n>>> : "))

    if MenuAwal == 1:
        print("\nIni adalah list Kode kota yang bisa anda input :")
        print("Kode Kota | Nama Kota")
        scrap.CariDataKota()
        MenuDepan()
    elif MenuAwal == 2:
        inputkota = int(input("\nSilahkan Masukan Kode Anda : "))
        # memasukan url web yang akan di scrapping
        url = f'https://jadwalsholat.pkpu.or.id/monthly.php?id={inputkota}'

        # membuat variable contents yang mana berisi package perintah request
        # perintah request ditambah .get(url) berisi variable yang berisi url web
        contents = requests.get(url)
        response = BeautifulSoup(contents.text, "html.parser")
        data = response.find_all('tr', 'table_highlight')
        data = data[0]

        sholat = {}
        i = 0
        for d in data:
            if i == 1:
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

        print(f'\n{sholat}')
        # scrap.CariWaktuSholat()
        MenuAkhir()


def MenuAkhir():
    # Take input from user
    print('''\n==========================================
    \nApakah anda ingin kembali ke menu awal ?\nKetik Y untuk IYA atau N bila tidak.
    \n==========================================''')
    ulang_lagi = input('>>> : ')

    # If user types Y, run the calculate() function
    if ulang_lagi == 'Y':
        MenuDepan()

    # If user types N, say good-bye to the user and end the program
    elif ulang_lagi == 'N':
        print('>>>> Terima Kasih, Sampai Jumpa Lagi !! <<<<')

    #
    else:
        print('\nPerintah tidak dikenal !! Masukan input yang sesuai !')
        MenuAkhir()