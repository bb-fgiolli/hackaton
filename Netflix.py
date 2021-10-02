from seleniumwire import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import math
import re
import time
import requests
from bs4 import BeautifulSoup
import json
import re

class Netflix(): 
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.top_10_inicio = self.scraping()
        self.series_xpath = '/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div/div[1]/ul/li[3]/a'
        self.series = self.xpath(self.driver, self.series_xpath)
        self.movies_xpath = '/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div/div[1]/ul/li[4]/a'
        self.movies = self.xpath(self.driver, self.movies_xpath)
    
    def scroll_(self, driver, xpath=False):
        """Este método scrolea, encuentra el top 10 y imprime los nombres"""
        Y = driver.execute_script('return scrollY')
        max_Y = driver.execute_script('return scrollMaxY')
        while Y != max_Y:
            driver.execute_script('scrollTo(0, scrollMaxY)')
            Y = math.ceil(float(driver.execute_script('return scrollY')))
            time.sleep(4)
            max_Y = driver.execute_script('return scrollMaxY')
        next_elements = driver.find_element_by_css_selector('#row-1 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(3)')
        next_elements.click()
        time.sleep(4)   
        
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        top_10 = []
        n=0
        while True:
            contenedor = soup.find('div', {'id':"title-card-1-" + str(n), 'class':'title-card title-card-top-10'})
            top_10.append(contenedor)
            n+=1

            if n == 10:
                break
        if xpath ==False:
            top_10_inicio = top_10
            return top_10_inicio
        else:
            series_xpath = '/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div/div[1]/ul/li[3]/a'
            series = xpath(driver, series_xpath)
            movies_xpath = '/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div/div[1]/ul/li[4]/a'
            movies = xpath(driver, movies_xpath)
            print('FIN?')



        



    def xpath(self, xpath):
        find_generic_xpath = self.driver.find_elements_by_xpath(xpath)
        find_generic_xpath[0].click()
        top_ten = self.scroll_(self.driver, xpath=xpath)
        return top_ten


    def scraping(self):
        """ingresa a netflix con usuario y devuelve un driver (?)"""
        vpn = 1
        print('--- INICIANDO en Netflix ---')
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--incognito")
        # driver = webdriver.Chrome(chrome_options=chrome_options)
        # driver.maximize_window()
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.netflix.com/ar/login')
        self.driver.implicitly_wait(10)


        user = self.driver.find_elements_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div')
        user[0].click()

        user_path = self.driver.find_elements_by_xpath('//*[@id="id_userLoginId"]')
        user_path[0].send_keys("marianoble1154@gmail.com")
        user_path[0].send_keys(Keys.TAB)
        pass_ = self.driver.find_elements_by_xpath('//*[@id="id_password"]')
        pass_[0].send_keys('darwin1154*')
        pass_[0].send_keys(Keys.ENTER)
        time.sleep(1)
        augusto = self.driver.find_elements_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a/div/div')
        time.sleep(2)
        augusto[0].click()
        time.sleep(2)
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
        self.driver = webdriver.Firefox()
        top_10_inicio = self.scraping()
        series_xpath = '/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div/div[1]/ul/li[3]/a'
        series = self.xpath(self.driver, series_xpath)
        movies_xpath = '/html/body/div[2]/div/div/div[1]/div[1]/div[1]/div/div[1]/ul/li[4]/a'
        movies = self.xpath(self.driver, movies_xpath)
