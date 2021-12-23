import requests 
from bs4 import BeautifulSoup 

url_prisjakt = "https://www.prisjakt.no/tema/dagens-tilbud"
print("Hei")
html_text = requests.get(url_prisjakt).text
soup = BeautifulSoup(html_text, 'lxml')
products = soup.find('ul', class_= 'OffersGrid-sc-812954-0 SEiei DealsGrid-sc-1xqx86j-6 hzxONb deals-grid' )
print(products)
print("hris")