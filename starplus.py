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
class StarPlus():
    def __init__(self):
        self.login_url = 'https://www.starplus.com/es-419/login'
        self.cats = [] ###Lista de los contenidos a pasar a un json###
        self.scraping()
    def scraping(self):
        ###Primero iniciamos sesión y elegimos un usuario cualquiera###
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.starplus.com/es-419/login")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys("arturomontalvo1154@gmail.com")
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys("darwin1154")
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/main/div/div/section/ul/div[1]/div/div').click()
        ###Una vez en la página scroll hasta el fondo para que carguen todas los rieles###
        Y = self.driver.execute_script('return scrollY')
        max_Y = self.driver.execute_script('return scrollMaxY')
        while Y != max_Y:
            self.driver.execute_script('scrollTo(0, scrollMaxY)')
            Y = math.ceil(float(self.driver.execute_script('return scrollY')))
            time.sleep(8)
            max_Y = self.driver.execute_script('return scrollMaxY')
        ###Ahora buscamos los 10 del main###
        collections = self.driver.find_elements_by_css_selector("#home-collection > div")
        for collection in collections[9:]:
            try:
                category_title = collection.find_element_by_tag_name("h4").text
            except:
                print("Esto no es una categoría")
            cat_main = {"Pais": "AR", "Type":None, "Top":None, "Plataforma":None}
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
            cat_main["Plataforma"] = "StarPlus"
            self.cats.append(cat_main)
            print(cat_main)
            break
        ###Categoría películas###
        self.driver.find_element_by_xpath('/html/body/div/div/div[3]/header/nav/ul/span[5]/a/p').click()
        collections = self.driver.find_elements_by_css_selector(".in-view > div")
        for collection in collections:
            try:
                category_title = collection.find_element_by_tag_name("h4").text
            except:
                print("Esto no es una categoría")
            cat_mov = {"Pais": "AR", "Type":None, "Top":None, "Plataforma":None}
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
            cat_mov["Plataforma"] = "StarPlus"
            self.cats.append(cat_mov)
            print(cat_mov)
            break
        ###Categoría series###
        self.driver.find_element_by_xpath('/html/body/div/div/div[3]/header/nav/ul/span[6]/a/p').click()
        collections = self.driver.find_elements_by_css_selector(".in-view > div")
        for collection in collections:
            try:
                category_title = collection.find_element_by_tag_name("h4").text
            except:
                print("Esto no es una categoría")
            cat_ser = {"Pais": "AR", "Type":None, "Top":None, "Plataforma":None}
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
            cat_ser["Plataforma"] = "StarPlus"
            self.cats.append(cat_ser)
            print(cat_ser)
            break
        json_object = json.dumps(self.cats , indent = 4)
        return json_object