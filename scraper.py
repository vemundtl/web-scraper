from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

url_prisjakt = "https://www.prisjakt.no/tema/dagens-tilbud"

# Opening up connection, grabbing page 
uClient = uReq(url_prisjakt)
page_html = uClient.read()
uClient.close()

# html parsing 
page_soup = soup(page_html, "html.parser")

#grabs column with matches 
containers = page_soup.findAll("div", {"class" : "offer-product"})
test = []
title = containers[0].div.p.text
test.append(title)
