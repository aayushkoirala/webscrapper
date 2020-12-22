from selenium import webdriver
import pandas as pd
#import requests
from bs4 import BeautifulSoup

options = webdriver.Chromeoptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-d')

url = 'https://mystudentrecord.ucmerced.edu/pls/PROD/xhwschedule.P_ViewSchedule'

page = requests.get(url)
#print(page.text)

soup = BeautifulSoup(page.text, 'html.parser')

print(soup)


