from selenium import webdriver
from bs4 import BeautifulSoup
import time
import math
import json

user = "support@bb.vision"
passw = "KLM2012a"

class Disney:
    def __init__(self):
        self.base_url = "https://www.disneyplus.com/"
        self.movie_url = "https://www.disneyplus.com/movies"
        self.serie_url = "https://www.disneyplus.com/series"
    
    def scraping(self):
        driver = webdriver.Firefox()
        driver.get(self.base_url)
        elem = driver.find_element_by_css_selector("a.btn-secondary:nth-child(1)").click()
        driver.implicitly_wait(100)
        form = driver.find_element_by_xpath('//*[@id="dssLogin"]')
        if form.find_element_by_xpath('//*[@id="email"]'):
            form.find_element_by_xpath('//*[@id="email"]').send_keys(user)
            print("encontrado")
        driver.find_element_by_css_selector(".fESovW").click()
        driver.find_element_by_css_selector("#password").send_keys(passw)
        time.sleep(2)
        driver.find_element_by_class_name("jSauOQ").click()
        driver.find_element_by_css_selector(".WvPzN").click()
        time.sleep(10)
        Y = driver.execute_script('return scrollY')
        max_Y = driver.execute_script('return scrollMaxY')
        while Y != max_Y:
            driver.execute_script('scrollTo(0, scrollMaxY)')
            Y = math.ceil(float(driver.execute_script('return scrollY')))
            time.sleep(8)
            max_Y = driver.execute_script('return scrollMaxY')
        collections = driver.find_elements_by_css_selector("#home-collection > div")
        cats = []
        category_title= collections[10].find_element_by_tag_name("h4").text
        contenidos = collections[10].find_elements_by_class_name("image-container")[:10]
        cat = {"Plataforma":None, "Top":None, "Type":None}
        contenido_titles = []
        top = 0
        for contenido in contenidos:
            top += 1
            contenido_title = str(top) + ". " + contenido.get_attribute("alt")
            contenido_titles.append(contenido_title)
        cat["Plataforma"] = "Disney+"
        cat["Top"] = contenido_titles
        cat["Type"] = "Overall"
        cats.append(cat)
        category_title= collections[24].find_element_by_tag_name("h4").text
        contenidos = collections[24].find_elements_by_class_name("image-container")[:10]
        cat = {"Plataforma":None, "Top":None, "Type":None}
        contenido_titles = []
        top = 0
        for contenido in contenidos:
            top += 1
            contenido_title = str(top) + ". " + contenido.get_attribute("alt")
            contenido_titles.append(contenido_title)
        cat["Plataforma"] = "Disney+"
        cat["Top"] = contenido_titles
        cat["Type"] = "Kids"
        cats.append(cat)
        # Serializing json

        driver.get(self.movie_url)
        contenidos = driver.find_elements_by_class_name("image-container")[0:10]
        cat = {"Plataforma":None, "Top":None, "Type":None}
        contenido_titles = []
        top = 0
        for contenido in contenidos:
            top += 1
            contenido_title = str(top) + ". " + contenido.get_attribute("alt")
            contenido_titles.append(contenido_title)
        cat["Plataforma"] = "Disney+"
        cat["Top"] = contenido_titles
        cat["Type"] = "Movies"
        cats.append(cat)

        driver.get(self.serie_url)
        contenidos = driver.find_elements_by_class_name("image-container")[0:10]
        cat = {"Plataforma":None, "Top":None, "Type":None}
        contenido_titles = []
        top = 0
        for contenido in contenidos:
            top += 1
            contenido_title = str(top) + ". " + contenido.get_attribute("alt")
            contenido_titles.append(contenido_title)
        cat["Plataforma"] = "Disney+"
        cat["Top"] = contenido_titles
        cat["Type"] = "Series"
        cats.append(cat)

        json_object = json.dumps(cats, indent = 4)

        # Writing to sample.json
        with open("json.json", "w") as outfile:
            outfile.write(json_object)