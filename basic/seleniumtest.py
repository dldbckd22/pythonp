from bs4 import BeautifulSoup 
from selenium import webdriver
import time

driver = webdriver.Chrome('.\selenium\chromedriver.exe')
driver.get('https://www.istarbucks.co.kr/index.do')
time.sleep(10)

loca= driver.find_elements_by_class_name('ally')
loca.click()
time.sleep(10)