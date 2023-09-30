import requests
from bs4 import BeautifulSoup


def extract_data():
    try:
        link = requests.get('https://www.bmkg.go.id/')
        # print(link.status_code)
    except Exception:
        return None

    if link.status_code == 200:
        src = BeautifulSoup(link.text, 'html.parser')
        temp = src.find('div', {'class': 'gempabumi-home-bg margin-top-13'})
        temp = temp.findChildren('li')

        i = 1
        waktu = None
        magnitude = None
        kedalaman = None
        koordinat = None
        lokasi = None
        dirasakan = None

        for tem in temp:
            # print(i, tem)
            if i == 1:
                waktu = tem.text.split(', ')
                tanggal = waktu[0]
                jam = waktu[1]
            elif i == 2:
                magnitude = tem.text
            elif i == 3:
                kedalaman = tem.text
            elif i == 4:
                koordinat = tem.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 5:
                lokasi = tem.text
            elif i == 6:
                dirasakan = tem.text
            i = i + 1


    data = dict()
    data['tanggal'] = tanggal
    data['jam'] = jam
    data['magnitude'] = magnitude
    data['kedalaman'] = kedalaman
    data['ls'] = ls
    data['bt'] = bt
    data['lokasi'] = lokasi
    data['dirasakan'] = dirasakan
    return data


def view_data(result):
    # print(result)
    print("\nGEMPA BUMI TERKINI")
    print(f"Tanggal : {result['tanggal']}")
    print(f"Jam : {result['jam']}")
    print(f"Magnitude : {result['magnitude']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Kordinato : LS =  {result['ls']} BT = {result['bt']}")
    print(f"Lokasi : {result['lokasi']}")
    print(f"Dirasakan : {result['dirasakan']}")
