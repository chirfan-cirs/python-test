import csv
import requests
from bs4 import BeautifulSoup

link = requests.get('https://www.kompas.com/')

if link.status_code == 200:
    src = BeautifulSoup(link.text, 'html.parser')
    result = src.find('div', {'class': 'most__wrap clearfix'})
    result = result.findChildren('h4')
    data = []

    i = 1

    for news in result:
        d = {'news number': f'Title {i}', 'news': news.text}
        i += 1
        data.append(d)

    filename = 'kompas-scrap.csv'
    with open(filename, 'wt+', newline='') as f:
        w = csv.DictWriter(f, ['news number', 'news'])
        w.writeheader()

        for row in data:
            w.writerow(row)
