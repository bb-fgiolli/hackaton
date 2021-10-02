from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import math
import re
import time
import requests
from bs4 import BeautifulSoup
import json
import re
import itertools

class Netflix(): 
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.top_10_inicio = self.scraping()
        self.series_xpath = '/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div/div[1]/ul/li[3]/a'
        self.movies_xpath = '/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div/div[1]/ul/li[4]/a'
    


    def scraping(self, kids=False):
        """ingresa a netflix con usuario y devuelve un driver (?)"""
        self.urls = 'https://www.netflix.com/browse', 'https://www.netflix.com/browse/genre/83', 'https://www.netflix.com/browse/genre/34399'
        self.urls_kids = 'https://www.netflix.com/Kids', 'https://www.netflix.com/browse/genre/2496491', 'https://www.netflix.com/browse/genre/2495600'
        vpn = 1
        print('--- INICIANDO en Netflix ---')
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--incognito")
        # driver = webdriver.Chrome(chrome_options=chrome_options)
        # driver.maximize_window()
        self.driver.get('https://www.netflix.com/ar/login')
        self.driver.implicitly_wait(4)

        user = self.driver.find_elements_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div')
        user[0].click()
        user_path = self.driver.find_elements_by_xpath('//*[@id="id_userLoginId"]')
        user_path[0].send_keys("marianoble1154@gmail.com")
        user_path[0].send_keys(Keys.TAB)
        pass_ = self.driver.find_elements_by_xpath('//*[@id="id_password"]')
        pass_[0].send_keys('darwin1154*')
        pass_[0].send_keys(Keys.ENTER)
        time.sleep(1)
        if kids == True:
            kids = self.driver.find_elements_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]/div/a/div/div')
            time.sleep(2)
            kids[0].click()
            time.sleep(2)
            inicio_top_10 = self.scroll(self.urls_kids[0])
            series_top_10 = self.scroll(self.urls_kids[1])
            peliculas_top_10 = self.scroll(self.urls_kids[2])
            inicio_top_10_payload = {"Pais":"AR","Plataforma":'Netflix', "Top":inicio_top_10, "Type":None}
            series_top_10_payload = {"Pais":"AR","Plataforma":'Netflix', "Top":series_top_10, "Type":None}
            peliculas_top_10_payload = {"Pais":"AR","Plataforma":'Netflix', "Top":peliculas_top_10, "Type":None}
            payloads = []
            payloads.append(inicio_top_10_payload)
            payloads.append(series_top_10_payload)
            payloads.append(peliculas_top_10_payload)
        else:
            augusto = self.driver.find_elements_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a/div/div')
            time.sleep(2)
            augusto[0].click()
            time.sleep(2)
            inicio_top_10 = self.scroll(self.urls[0])
            series_top_10 = self.scroll(self.urls[1])
            peliculas_top_10 = self.scroll(self.urls[2])
            top = 1
            inicio_top_10_payload = {"Pais":"AR","Plataforma":'Netflix', "Top":inicio_top_10, "Type":None}
            series_top_10_payload = {"Pais":"AR","Plataforma":'Netflix', "Top":series_top_10, "Type":None}
            peliculas_top_10_payload = {"Pais":"AR","Plataforma":'Netflix', "Top":peliculas_top_10, "Type":None}
            payloads = []
            payloads.append(inicio_top_10_payload)
            payloads.append(series_top_10_payload)
            payloads.append(peliculas_top_10_payload)

    
    def scroll(self, url):
        self.driver.get(url)
        Y = self.driver.execute_script('return scrollY')
        max_Y = self.driver.execute_script('return scrollMaxY')
        while Y != max_Y:
            self.driver.execute_script('scrollTo(0, scrollMaxY)')
            Y = math.ceil(float(self.driver.execute_script('return scrollY')))
            time.sleep(4)
            max_Y = self.driver.execute_script('return scrollMaxY')
        next_elements = self.driver.find_element_by_css_selector('#row-1 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(3)')
        next_elements.click()
        time.sleep(4)   
        
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        top_10 = []
        n=0
        while True:
            contenedor = soup.find('div', {'id':"title-card-1-" + str(n), 'class':'title-card title-card-top-10'})
            top_10.append(contenedor)
            n+=1

            if n == 10:
                break
        
        top_10_inicio = top_10
        return top_10_inicio
            


    def main(self):
        json1 = self.scraping()
        print(json1)
        json2 = self.scraping(kids=True)
        json3 = json1 + json2
        print(json3)
        return json3
        # top_10_inicio = self.scraping()
        # series_xpath = '/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div/div[1]/ul/li[3]/a'
        # series = self.xpath(self.driver, series_xpath)
        # movies_xpath = '/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div/div[1]/ul/li[4]/a'
        # movies = self.xpath(self.driver, movies_xpath)
