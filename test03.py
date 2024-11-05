import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#窗口最大化
driver.maximize_window()
driver.get("https://www.bilibili.com/")
#找到搜索按钮，点击,默认是第一个
#driver.find_element(By.CLASS_NAME,'channel-link').click()
#需要选着第几个的话，加下标
driver.find_element(By.CLASS_NAME,'channel-link')[4].click()
time.sleep(20)
driver.close()