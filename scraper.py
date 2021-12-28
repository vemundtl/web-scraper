from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains    
import pandas as pd  
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.prisjakt.no")

best_offers = driver.find_element(By.XPATH, "//a[@class='TopLevelLink-sc-1niqwua-8 cauozV']").click()


try: 
    best_offers_list = WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='OffersGrid-sc-812954-0 SEiei DealsGrid-sc-1xqx86j-6 hzxONb deals-grid']")))
    offers = best_offers_list.find_elements(By.XPATH, "//li[@class='OffersGridItem-sc-812954-1 jjGPxW']")
    offers_as_dict = []
    for i in range(24):
        # name = offers[i].find_elements(By.XPATH, "//div//a//div[@class='CardContent--1rgxuny Content-sc-1i3jpuu-1 gEzdvD']//span").text
        # name = offers[i].find_elements(By.XPATH, "//div[@class='Card--1ybcv3v fyicOL Card-sc-1i3jpuu-0 iksJeT']//a[@class='InternalLink-sc-t916l0-1 dHlSTu CardActionArea--1q831uy bYceJN']//div[@class='CardContent--1rgxuny Content-sc-1i3jpuu-1 gEzdvD']//span[@class='Text--63zgu0 bAgiyD titlemediumtext']")
        attributes = offers[i].text.splitlines()
        procentage = attributes[0]
        name = attributes[1]
        category = attributes[2]
        if(len(attributes) == 5):
            price = attributes[4]
        else: 
            price = attributes[5]
        offer = {
            "procentage" : procentage,
            "name" : name, 
            "category" : category, 
            "price" : price,
        }
        offers_as_dict.append(offer)          
    
except: 
    driver.quit()


driver.quit()

df_data = pd.DataFrame(offers_as_dict)
df_data.to_excel("prisjakt_tilbud.xlsx", index=False)