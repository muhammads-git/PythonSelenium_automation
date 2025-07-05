import selenium
import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

def setup_function():
    hub_url = 'http://172.27.96.1:4444/wd/hub'
    global driver
    option = webdriver.FirefoxOptions()
    driver = webdriver.Remote(
        command_executor=hub_url,
        options = option
    )
    driver.implicitly_wait(5)

def teardown_function():
    driver.quit()


def test_cricbuzz_automation():
# get cricbuzz url

    driver.get('https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting')
    time.sleep(3)   # optional can be replaced with explicit wait
    
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
        
    # lets assert it
    assert len(cols_table) == 6, "Column count mismatch"
    assert len(rows_table) > 0, "No rows found in the table"
