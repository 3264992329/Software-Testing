import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com/')

#绝对路径
#driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/div/div/ul/li[1]/a/span[1]").click()

#相对路径，根据id定位
#driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys("原神启动")
#driver.find_element(By.XPATH,'//input[@id="su"]').click()

#相对路径，组合条件查询
#driver.find_element(By.XPATH,'//*[@id="s-top-left"]/a[4]').click()
#driver.find_element(By.XPATH,'//*[@class="s-top-left-new s-isindex-wrap"]/a[4]').click()

#通过子元素去找父元素
#driver.find_element(By.XPATH,'//*[@class="s-top-left-new s-isindex-wrap"]/a[2]').click()

#通过文本去查找
#driver.find_element(By.XPATH,'//span[text()="中共中央政治局召开会议"]').click()

#根据同级弟弟定位
#driver.find_element(By.XPATH,'//a[contains(text(),"贴吧")]/following::a[1]').click()
# #根据同级哥哥定位
driver.find_element(By.XPATH,'//a[contains(text(),"贴吧")]/preceding::a[2]').click()


time.sleep(5)