from selenium import webdriver
import pandas as pd
#import timeit

#start_time = timeit.default_timer()
#from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

url = 'https://mystudentrecord.ucmerced.edu/pls/PROD/xhwschedule.p_selectsubject'

wd = webdriver.Chrome('chromedriver', options=options)
wd.get(url)

#status = wd.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr[11]/td[1]/input").is_selected()
#print(status)

#print('abc')
wd.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr[11]/td[1]/input").click()

#status = wd.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr[11]/td[1]/input").is_selected()
#print(status)

#print('efg')
wd.find_element_by_xpath("/html/body/div[3]/form/input").click()
#wd.implicitly_wait(3)
#print('1')

#print('2')

#with open("html.txt", "w") as file:
  #file.write(html)

html = wd.page_source
df = pd.concat(pd.read_html(html))

rdf = df[['Course #', 'Seats Avail']]
df_print = rdf[rdf['Course #'] == 'ANTH-003-06D']

for index, row in df_print.iterrows():
  if row['Seats Avail'] == 'Closed':
    print('The course ' + row['Course #'] + ' is currently ' + row['Seats Avail']+'.')
  else:
    print('The course ' + row['Course #'] + ' currently has ' + row['Seats Avail']+' spot(s) left.')

#df.to_csv('c_df.csv')
#print(timeit.default_timer() - start_time)

#print(df)
#print(html)