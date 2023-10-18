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
        data['media1'] = media1
        data['media2'] = media2
        data['media3'] = media3
        data['media4'] = media4
        data['media5'] = media5
        return data

def view_data(result):
    print("Data Scraping Kompas.com")
    dat = result['media1'], result['media2'], result['media3'], result['media4'], result['media5']
    index = range(1, 6)
    for x, y in zip(index, dat):
        print(f"Data berita Populer No {x}. {y}")










# import requests
# from bs4 import BeautifulSoup
#
#
# def extract_data():
#     try:
#         link = requests.get('https://www.kompas.com/')
#         print(link.status_code)
#     except Exception:
#         return None
#
#     if link.status_code == 200:
#         src = BeautifulSoup(link.text, 'html.parser')
#         result = src.find('div', {'class': 'most__wrap clearfix'})
#         result = result.findChildren('h4')
#
#         i = 1
#         most_title1 = None
#         most_title2 = None
#         most_title3 = None
#         most_title4 = None
#         most_title5 = None
#
#         for res in result:
#             # print(i, res)
#             if i == 1:
#                 most_title1 = res.text
#             elif i == 2:
#                 most_title2 = res.text
#             elif i == 3:
#                 most_title3 = res.text
#             elif i == 4:
#                 most_title4 = res.text
#             elif i == 5:
#                 most_title5 = res.text
#             i = i + 1
#
#         data = dict()
#         data['one'] = most_title1
#         data['two'] = most_title2
#         data['three'] = most_title3
#         data['four'] = most_title4
#         data['five'] = most_title5
#         return data
#
#
# def view_data(result):
#     print(result)
#     print("THE MOST READ NEWS FROM Kompas.com")
#
#
#     i = range(1, 6)
#     res = result['one'], result['two'], result['three'], result['four'], result['five']
#     for x, y in zip(i, res):
#         print(f"Most Read News Number {x} : {y}")
#
#     print(f"Most Read News Number 1 : {result['one']}")
#     # print(f"Most Read News Number 2 : {result['two']}")
#     # print(f"Most Read News Number 3 : {result['three']}")
#     # print(f"Most Read News Number 4 : {result['four']}")
#     # print(f"Most Read News Number 5 : {result['five']}")
