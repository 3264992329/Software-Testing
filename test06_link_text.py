from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.bilibili.com/")
driver.find_element(By.LINK_TEXT,'番剧').click()
sleep(10)