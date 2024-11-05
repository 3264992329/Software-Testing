from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com/')
#driver.get('https://www.bilibili.com/')

#css，根据id定位
#driver.find_element(By.CSS_SELECTOR,'#kw').send_keys('影石')
#driver.find_element(By.CSS_SELECTOR,'#su').click()

#css，根据class定位
#driver.find_element(By.CSS_SELECTOR,'.nav-search-input').send_keys('哈哈哈')
#driver.find_element(By.CSS_SELECTOR,'.nav-search-btn').click()

#css，根据属性值定位
#driver.find_element(By.CSS_SELECTOR,'[name="wd"]').send_keys("123")
#driver.find_element(By.CSS_SELECTOR,'#su').click()

#css,根据标签定位
#driver.find_element(By.CSS_SELECTOR,"a[href='//www.bilibili.com/anime/']").click()
#模糊查找
#driver.find_element(By.CSS_SELECTOR,"a[href*='bilibili.com/movie/']").click()
#根据开头匹配
#driver.find_element(By.CSS_SELECTOR,"a[href^='//www.bilibili.com/ani']").click()
#根据结尾匹配
#driver.find_element(By.CSS_SELECTOR,"a[href$='com/anime/']").click()

#组合查找
#driver.find_element(By.CSS_SELECTOR,'input.nav-search-input').click()

#定位子元素
#组合id进行定位
#driver.find_element(By.CSS_SELECTOR,"div#s-top-left>a").click()
#组合class进行定位
#driver.find_element(By.CSS_SELECTOR,"div.s-top-left-new.s-isindex-wrap>a").click()
#加上:nth-child()对子元素进行定位
#driver.find_element(By.CSS_SELECTOR,"div#s-top-left>a:nth-child(3)").click()
#find_elements加上[n]进行定位
#driver.find_elements(By.CSS_SELECTOR,"div#s-top-left>a")[3].click()

#通过复制
driver.find_element(By.CSS_SELECTOR,"#s-top-left > a:nth-child(5)").click()
sleep(5)