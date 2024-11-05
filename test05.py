from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.bilibili.com/")
#driver.find_element(By.CLASS_NAME,'channel-link').click()
elements = driver.find_elements(By.CLASS_NAME,'channel-link')
#elements[5].click()
for element in elements:
    print(element.text)
    element.click()
sleep(5)