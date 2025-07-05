import selenium
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(5)

# get cricbuzz url
driver.get('https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting')
time.sleep(3)
cols_table = driver.find_elements(By.XPATH, '//*[@id="page-wrapper"]/div[3]/div[2]/div/div/div[1]/div')
rows_table = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/div')
print('Total Columns are: ',len(cols_table))
print('Total Rows are: ',len(rows_table))

print(":::::::::::::RANKING::::::::::::::::")

for cols in cols_table:
    print(f"{cols.text}", end=' ')
print("\n:::::::::::::PLAYERS::::::::::::::::")

for row in rows_table:
    print(f'{row.text}', end=' ')
print("\n:::::::::::::END::::::::::::::::")
      

driver.quit()

