from selenium import webdriver
import pandas as pd
#import requests
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')



url = 'https://mystudentrecord.ucmerced.edu/pls/PROD/xhwschedule.p_selectsubject'

wd = webdriver.Chrome('chromedriver', options=options)
wd.get(url)


wd.implicitly_wait(10)
html = wd.page_source
df = pd.read_html(html)

print(df[0])
