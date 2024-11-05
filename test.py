import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#窗口最大化
driver.maximize_window()
driver.get("https://www.bilibili.com/")
#找到搜索框，输入：原神启动
driver.find_element(By.CLASS_NAME,'nav-search-input').send_keys("原神启动")
#找到搜索按钮，点击搜索
driver.find_element(By.CLASS_NAME,'nav-search-btn').click()
time.sleep(3)
driver.close()