import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

op = webdriver.ChromeOptions()
# op.add_argument('headless')
driver = webdriver.Chrome(options=op)



driver.get('https://www.sec.gov/edgar/search/#/category=custom&entityName=TSLA&forms=10-Q')

time.sleep(3)

a = driver.find_element(By.CSS_SELECTOR, 'td.filetype')
print(a.text)

driver.quit()