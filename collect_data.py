import time

import pickle as pk

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


with open('data/sp500tickers.pickle', 'rb') as f:
    tickers = pk.load(f)

op = webdriver.ChromeOptions()
# op.add_argument('headless') # Headers issue
driver = webdriver.Chrome(options=op)

reports = {}
for ticker in tickers:
    try:
        driver.get(f'https://www.sec.gov/edgar/search/#/category=custom&entityName={ticker}&forms=10-Q')
        time.sleep(2)
        elems = driver.find_elements(By.CSS_SELECTOR, 'td.filetype>a')
        links = [elem.get_attribute('href') for elem in elems]

        reports[ticker] = links
    except:
        continue

driver.quit()

with open('data/reports.pickle', 'wb') as f:
    pk.dump(reports, f, pk.HIGHEST_PROTOCOL)

