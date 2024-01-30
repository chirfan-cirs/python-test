import csv
import requests
from bs4 import BeautifulSoup

def extract_data():
    try:
        link = requests.get('https://www.kompas.com/')
        print(link.status_code)
    except Exception:
        return None

    if link.status_code == 200:
        src = BeautifulSoup(link.text, 'html.parser')
        result = src.find('div', {'class': 'most__wrap clearfix'})
        result = result.findChildren('h4')
        data = []

        i = 1
        media1 = None
        media2 = None
        media3 = None
        media4 = None
        media5 = None

        for res in result:
            if i == 1:
                media1 = res.text
            elif i == 2:
                media2 = res.text
            elif i == 3:
                media3 = res.text
            elif i == 4:
                media4 = res.text
            elif i == 5:
                media5 = res.text
            i = i + 1

        data = dict()
        data['No 1'] = media1
        data['No 2'] = media2
        data['No 3'] = media3
        data['No 4'] = media4
        data['No 5'] = media5
        return data

def save_csv(data):
    filename = 'kompas-scrap.csv'
    with open(filename, 'wt+', newline='') as f:
        w = csv.DictWriter(f, ['news number', 'news'])
        w.writeheader()

        for key, value in data.items():
            w.writerow({'news number': key, 'news': value})


def view_data(result):
    print("Data Scraping Kompas.com")
    dat = result['No 1'], result['No 2'], result['No 3'], result['No 4'], result['No 5']
    index = range(1, 6)
    for x, y in zip(index, dat):
        print(f"Data berita Populer No {x}. {y}")





#
# import requests
# from bs4 import BeautifulSoup
# import csv
#
# # Send a GET request to the target website
# url = "https://www.goodreads.com/list/show/18816.Books_You_Must_Read_"
# response = requests.get(url)
#
# if response.status_code == 200:
#     # Parse the HTML content of the page
#     soup = BeautifulSoup(response.content, "html.parser")
#
#     # Find all book names and author names using CSS selectors
#     book_selector = "a.bookTitle span"
#     auth_selector = "span[itemprop='author']"
#
#     book_data = []
#
#     # Find all book names and author names using CSS selectors
#     book_names = soup.select(book_selector)
#     auth_names = soup.select(auth_selector)
#
#     # Extract text from the selected elements
#     for book_name, auth_name in zip(book_names, auth_names):
#         book_name_text = book_name.get_text(strip=True)
#         auth_name_text = auth_name.get_text(strip=True)
#
#         book_data.append([book_name_text, auth_name_text])
#
#     csv_filename = "book_list.csv"
#
#     # Write the data to a CSV file
#     with open(csv_filename, mode="w", encoding="utf-8", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Book Name", "Author Name"])  # Write header row
#         writer.writerows([book_data])
#     print(f"Data has been scraped and saved to {csv_filename}")
# else:
#     print(f"Failed to retrieve data. Status code: {response.status_code}")