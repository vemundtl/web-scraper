from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

my_url = 'https://store.playstation.com/no-no/category/803cee19-e5a1-4d59-a463-0b6b2701bf7c/1'

# Opening up connection, grabbing page 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing 
page_soup = soup(page_html, "html.parser")

#grabs column with matches 
containers = page_soup.findAll("div", {"div", {"class" : "col-12"}}) 
games = soup.findAll("li", {"class" : "psw-cell"})