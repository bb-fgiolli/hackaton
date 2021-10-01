from selenium import webdriver
from bs4 import BeautifulSoup
import time
import math

user = "support@bb.vision"
passw = "KLM2012a"

url = "https://www.disneyplus.com/"

driver = webdriver.Firefox()
driver.get(url)
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
for collection in collections[2:]:
    try:
        category_title = collection.find_element_by_tag_name("h4").text
    except:
        print("Esto no es una categoría")
    cat = {"title":None, "contents":None}
    contenidos = collection.find_elements_by_class_name("image-container")
    contenido_titles = []
    for contenido in contenidos:
        contenido_title = contenido.get_attribute("alt")
        contenido_titles.append(contenido_title)
    cat["title"] = category_title
    cat["contents"] = contenido_titles[:10]
    cats.append(cat)
print(cats)