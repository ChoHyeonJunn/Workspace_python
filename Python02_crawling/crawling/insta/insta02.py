# -*- coding:utf-8 -*-

# pip install selenium
from selenium import webdriver
from bs4 import BeautifulSoup

tag = input('search tag : ')
url = 'https://www.instagram.com/explore/tags/' + tag

# Chrome webdriver 필요! (chrome 버전에 맞춰서 다운로드!!)
driver = webdriver.Chrome('C:/selenium/chromedriver.exe')

driver.implicitly_wait(3)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
div = soup.find_all('div', class_='KL4Bh')
print(div)
