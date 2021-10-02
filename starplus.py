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
cats = [] ###Lista de los contenidos a pasar a un json###

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

###Ahora buscamos los 10 del main###
collections = driver.find_elements_by_css_selector("#home-collection > div")
for collection in collections[9:]:
    try:
        category_title = collection.find_element_by_tag_name("h4").text
    except:
        print("Esto no es una categoría")
    cat_main = {"Type":None, "Top":None, "Platform ":None}
    contenidos = collection.find_elements_by_class_name("image-container")
    contenido_titles = []
    n = 0
    for contenido in contenidos:
        n += 1
        if n > 10:
            continue
        contenido_title = contenido.get_attribute("alt")
        contenido_titles.append(str(n) + ". " + contenido_title)
    cat_main["Type"] = 'Main'
    cat_main["Top"] = contenido_titles[:10]
    cat_main["Platform "] = "StarPlus"
    cats.append(cat_main)
    print(cat_main)
    break

###Categoría películas###
driver.find_element_by_xpath('/html/body/div/div/div[3]/header/nav/ul/span[5]/a/p').click()

collections = driver.find_elements_by_css_selector(".in-view > div")
for collection in collections:
    try:
        category_title = collection.find_element_by_tag_name("h4").text
    except:
        print("Esto no es una categoría")
    cat_mov = {"Type":None, "Top":None, "Platform ":None}
    contenidos = collection.find_elements_by_class_name("image-container")
    contenido_titles = []
    n = 0
    for contenido in contenidos:
        n += 1
        if n > 10:
            continue
        contenido_title = contenido.get_attribute("alt")
        contenido_titles.append(str(n) + ". " + contenido_title)
    cat_mov["Type"] = 'Movies'
    cat_mov["Top"] = contenido_titles[:10]
    cat_mov["Platform "] = "StarPlus"
    cats.append(cat_mov)
    print(cat_mov)
    break

###Categoría series###
driver.find_element_by_xpath('/html/body/div/div/div[3]/header/nav/ul/span[6]/a/p').click()

collections = driver.find_elements_by_css_selector(".in-view > div")
for collection in collections:
    try:
        category_title = collection.find_element_by_tag_name("h4").text
    except:
        print("Esto no es una categoría")
    cat_ser = {"Type":None, "Top":None, "Platform ":None}
    contenidos = collection.find_elements_by_class_name("image-container")
    contenido_titles = []
    n = 0
    for contenido in contenidos:
        n += 1
        if n > 10:
            continue
        contenido_title = contenido.get_attribute("alt")
        contenido_titles.append(str(n) + ". " + contenido_title)
    cat_ser["Type"] = 'Series'
    cat_ser["Top"] = contenido_titles[:10]
    cat_ser["Platform "] = "StarPlus"
    cats.append(cat_ser)
    print(cat_ser)
    break

with open('starplus.json', 'w') as f:
    json.dump(cats, f)

driver.close()
driver.quit()
print("script finalizado")
