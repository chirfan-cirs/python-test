import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the target website
url = "https://www.goodreads.com/list/show/18816.Books_You_Must_Read_"
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all book names and author names using CSS selectors
    book_selector = "a.bookTitle span"
    auth_selector = "span[itemprop='author']"

    book_data = []

    # Find all book names and author names using CSS selectors
    book_names = soup.select(book_selector)
    auth_names = soup.select(auth_selector)

    # Extract text from the selected elements
    for book_name, auth_name in zip(book_names, auth_names):
        book_name_text = book_name.get_text(strip=True)
        auth_name_text = auth_name.get_text(strip=True)

        book_data.append([book_name_text, auth_name_text])

    csv_filename = "book_list.csv"

    # Write the data to a CSV file
    with open(csv_filename, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Book Name", "Author Name"])  # Write header row
        writer.writerows([book_data])
    print(f"Data has been scraped and saved to {csv_filename}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")