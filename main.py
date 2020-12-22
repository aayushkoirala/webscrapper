from selenium import webdriver
import pandas as pd
#import requests
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')



url = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_base_stats_(Generation_VI)'

wd = webdriver.Chrome('chromedriver', options=options)
wd.get(url)
term ='body > div.pagebodydiv > form > table > tbody > tr:nth-child(7) > td:nth-child(1) > input[type=radio]'
button1 = wd.find_element_by_css_selector(term)
button1.click()

all_classes ='body > div.pagebodydiv > form > table > tbody > tr:nth-child(11) > td:nth-child(1) > input[type=radio]'

button2 = wd.find_element_by_css_selector(all_classes)
button2.click()
view = 'body > div.pagebodydiv > form > input[type=submit]'
button3 =wd.find_element_by_css_selector(view)
button3.click()

wd.implicitly_wait(10)
html = wd.page_source
df = pd.read_html(html)

print(df[0])
