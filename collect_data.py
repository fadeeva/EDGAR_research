from selenium import webdriver
from selenium.webdriver.chrome.options import Options

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

driver.get('https://www.sec.gov/edgar/search/#/category=custom&entityName=TSLA&forms=10-Q')