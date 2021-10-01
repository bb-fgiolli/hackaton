from typing import Type
import requests
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import math
import json

main_url = 'https://www.starplus.com/es-419/home'

###Primero iniciamos sesión y elegimos un usuario cualquiera###
driver = webdriver.Firefox()
driver.get("https://www.starplus.com/es-419/login")
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="email"]').send_keys("arturomontalvo1154@gmail.com")
driver.find_element_by_xpath('//*[@id="email"]').send_keys(Keys.ENTER)
driver.find_element_by_xpath('//*[@id="password"]').send_keys("darwin1154")
driver.find_element_by_xpath('//*[@id="password"]').send_keys(Keys.ENTER)
driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/main/div/div/section/ul/div[1]/div/div').click()

###Una vez en la página scroll hasta el fondo para que carguen todas los rieles###
Y = driver.execute_script('return scrollY')
max_Y = driver.execute_script('return scrollMaxY')
while Y != max_Y:
    driver.execute_script('scrollTo(0, scrollMaxY)')
    Y = math.ceil(float(driver.execute_script('return scrollY')))
    time.sleep(8)
    max_Y = driver.execute_script('return scrollMaxY')

###Ahora buscamos los contenidos y nos quedamos con los 10 primeros de cada sección###
collections = driver.find_elements_by_css_selector("#home-collection > div")
cats = []
for collection in collections[2:]:
    try:
        category_title = collection.find_element_by_tag_name("h4").text
    except:
        print("Esto no es una categoría")
    cat = {"title":None, "contents":None}
    contenidos = collection.find_elements_by_class_name("image-container")
    contenido_titles = []
    n = 0
    for contenido in contenidos:
        n += 1
        if n > 10:
            continue
        contenido_title = contenido.get_attribute("alt")
        contenido_titles.append(contenido_title)
    cat["title"] = category_title
    cat["contents"] = contenido_titles[:10]
    cats.append(cat)
print(cats)


with open('starplus.json', 'w') as f:
    json.dump(cats, f)

driver.close()
driver.quit()
print("script finalizado")