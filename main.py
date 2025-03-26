import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

#Библиотеки для работы с сайтом
import requests
from bs4 import BeautifulSoup
import lxml
#Для ссылок получение их
import re

# create webdriver object
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# enter keyword to search
keyword = "m"
url = "https://www.sberbank-ast.ru/purchaseList.aspx"
headers = {
    'Accept': '* / *',
    "User - Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 116.0.0.0Safari / 537.36OPR / 102.0.0.0(EditionYxGX)"
}
def input_search(keyword,url):
    # get geeksforgeeks.org
    driver.get(url=url)
    time.sleep(13)
    # get element
    element = driver.find_element(By.ID,"searchInput")
    element.click()
    search = driver.find_element(By.ID,'searchInput')
    search.send_keys(keyword)
    search.send_keys(Keys.ENTER)
def next_page(url):
    driver.get(url=url)
    time.sleep(2)
    # get element

    # element = driver.find_element(By.XPATH, "/html/body/form/div=[@class='master_open_content']/div[@class='container']/div/div[@id=pager]/span[@id='pagesControl']/span[-2]/span")

    element = driver.find_element(By.XPATH, "/ html / body / form / div[7] / div / div / div[7] / span / span[14] / span[1]")
    element.click()
    print(element)
    #element.click()
def find_elements(number:int = 2):
    str_money1 = '/html/body/form/div[7]/div/div/div[10]/div/div[1]/table/tbody/tr[1]/td[1]/div[3]/span[1]'
    number1 =    '/html/body/form/div[7]/div/div/div[10]/div/div[1]/table/tbody/tr[1]/td[2]/div[1]/span[1]'
    who_sell1 =  '/html/body/form/div[7]/div/div/div[10]/div/div[1]/table/tbody/tr[1]/td[2]/div[2]'
    what_sell1 = '/html/body/form/div[7]/div/div/div[10]/div/div[1]/table/tbody/tr[1]/td[2]/span'

    str_money = str_money1[:47] + str(number) + str_money1[48:]
    numbers = number1[:47] + str(number) + number1[48:]
    who_sell = who_sell1[:47] + str(number) + who_sell1[48:]
    what_sell = what_sell1[:47] + str(number) + what_sell1[48:]
    return str_money, numbers, who_sell, what_sell
def collecting_information(url,headers,keyword):
    # input_search(keyword=keyword,url=url)
    # time.sleep(3)
    # next_page(url)

    # src = requests.get(url, headers=headers).text
    # soup = BeautifulSoup(src, 'lxml')

    driver.get(url=url)
    time.sleep(28)
    for i in range(2,21):
        list_element = find_elements(i)
        print(driver.find_element(By.XPATH,list_element[0]).text)
        print(driver.find_element(By.XPATH,list_element[1]).text)
        print(driver.find_element(By.XPATH,list_element[2]).text)
        print(driver.find_element(By.XPATH,list_element[3]).text)

    # now_site=soup.find("span", format_="money")
    # Close browser
    driver.quit()
collecting_information(url=url,headers=headers,keyword=keyword)
