from bs4 import BeautifulSoup
from selenium import webdriver
import time

#네이버로그인
driver = webdriver.Chrome('./selenium/chromedriver.exe')
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
id = 'dldbckd22'
pw = 'gksrmf33!!'
driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'") 
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'") 

# driver.find_element_by_name('id').send_keys(id)
# driver.find_element_by_name('pw').send_keys(pw)
time.sleep(10)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

#지역검색
# driver = webdriver.Chrome('./selenium/chromedriver.exe')
# driver.get('https://www.istarbucks.co.kr/store/store_map.do?disp=quick')
# driver.get('https://www.istarbucks.co.kr/store/store_map.do?disp=quick')
# time.sleep(5)
# loca=driver.find_elements_by_css_selector('.loca_search a')
# loca.send_keys('\n')
# time.sleep(10)
# sido=driver.find_element_by_class_name('sido_arae_box')
# li=sido.find_element_by_tag_name('li')
# li[5].send.keys('\n')


#구글맵검색
# driver = webdriver.Chrome('./selenium/chromedriver.exe')
# driver.get('https://www.google.com/maps/?hl=ko')
# time.sleep(3)
# element1 = driver.find_element_by_id('searchboxinput')
# element1.send_keys('카카오')
# element2 = driver.find_element_by_id('searchbox-searchbutton')
# element2.click()
# time.sleep(10)
# pages = driver.page_source
# bs=BeautifulSoup(pages,'html.parser')
# itemtitle = bs.select('h3.section-result-title span')
# itemlocation=bs.select('span.section-result-location')
# print(itemtitle[0].string)
# print(itemlocation[0].string)