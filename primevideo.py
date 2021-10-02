from typing import Type
import requests
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver

#usuario = arturomontalvo1154@gmail.com
#password = darwin1154*

###Primero iniciamos sesión###
driver = webdriver.Firefox()
driver.get("https://www.primevideo.com/")
driver.implicitly_wait(10)

driver.find_element_by_xpath('//*[@id="pv-nav-sign-in"]').click()

driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys("arturomontalvo1154@gmail.com")
driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys("darwin1154*")
driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()

###Top 10 main###
collection = driver.find_elements_by_css_selector("div._2FMydd:nth-child(3)")
print(collection)

overall_contents = driver.find_elements_by_class_name('_2JmP8_')
for all in overall_contents:
    content = driver.find_elements_by_css_selector(all + '> div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)')
    title = content.get_attribute('aria-label')
    

contenido = driver.find_elements_by_css_selector("li._2JmP8_:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1) ")
print (contenido)

contenido2 = driver.find_elements_by_css_selector("div._2FMydd:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
print (contenido2)
#class="_2FMydd tst-faceted-carousel _17Zx0N"
#div._2FMydd:nth-child(3)

#driver.close()
#driver.quit()
print("script finalizado")
#li._2JmP8_:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1) 
#li._2JmP8_:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)
#div._2FMydd:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)