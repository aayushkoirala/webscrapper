from selenium import webdriver
import pandas as pd
#import requests
from bs4 import BeautifulSoup
import os
import csv

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

url = 'https://mystudentrecord.ucmerced.edu/pls/PROD/xhwschedule.p_selectsubject'

wd = webdriver.Chrome('chromedriver', options=options)
wd.get(url)
#status = wd.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr[11]/td[1]/input").is_selected()
#print(status)
print('abc')
wd.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr[11]/td[1]/input").click()

#status = wd.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr[11]/td[1]/input").is_selected()
#print(status)
print('efg')
wd.find_element_by_xpath("/html/body/div[3]/form/input").click()
wd.implicitly_wait(3)
print('1')
html = wd.page_source
print('2')
dataf = pd.read_html(html)
df = pd.concat(dataf)
#print(df)
df.to_csv('text.csv')
#df.to_csv('df.csv')
#print(df)
#with open("df.txt", "w") as file:
 # file.write(df.to_string())
#print(html)



