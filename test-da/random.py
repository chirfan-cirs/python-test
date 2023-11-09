news = {
    "title": "Xaxaxa",
    "date": "08 April",
    "view": 1532
},{
    "title": "asdasf",
    "date": "12 August",
    "view": 23234
},{
    "title": "erggsdf",
    "date": "31 Desember",
    "view": 52351
}

print(news)

for res in news:
    print(f"Judul berita: {res['title']} pada tanggal {res['date']} sudah di lihat {res['view']} kali")
