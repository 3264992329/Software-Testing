from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com/")
driver.find_element(By.ID,"kw").send_keys("软件测试")
driver.find_element(By.ID,"su").click()
sleep(3)
driver.close()