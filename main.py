import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    print("Successfully fetched the web page")
else:
    print("Failed to fetch the web page")
    
soup = BeautifulSoup(response.content, 'html.parser')

books = soup.find_all('article', class_='product_pod')

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    print(f"Title: {title}, Price: {price}")
    
