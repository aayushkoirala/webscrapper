import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://mystudentrecord.ucmerced.edu/pls/PROD/xhwschedule.P_ViewSchedule'

page = requests.get(url)
#print(page.text)

soup = BeautifulSoup(page.text, 'html.parser')

print(soup)
