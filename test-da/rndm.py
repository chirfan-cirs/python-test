import time
import random

news = {
    'title': 'Xaxaxxaxaxaxa',
    'date': time.ctime(),
    'view': random.seed(1)
},{
    'title': 'aasdasdwfwffw',
    'date': time.ctime(),
    'view': random.randint(1, 100)
},{
    'title': 'gdgafawfawfaw',
    'date': time.ctime(10.0),
    'view': random.randint(100, 1000)
}

for res, i in zip(news, range(1,5)):
    print("========================")
    print(f"Berita ke-{i}")
    print(f"Judul Berita            : {res['title']}")
    print(f"Waktu Berita diposting  : {res['date']}")
    print(f"Jumlah pembaca          : {res['view']}")