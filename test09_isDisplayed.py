from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_is_displayed():
    driver = webdriver.Chrome()
    #在页面加载超过1秒时，抛出异常
    #driver.set_page_load_timeout(1)
    driver.get('https://www.bilibili.com/')
    driver.maximize_window()
    #如果异步脚本执行时间超过设定的 1 秒，WebDriver 将抛出 TimeoutException
    driver.set_script_timeout(0.001)

    #检查元素是否在页面上可见
    #a = driver.find_element(By.XPATH,'(//a[@href="//www.bilibili.com/anime/"])[2]').is_displayed()
    #检查元素是否可交互
    a = driver.find_element(By.XPATH,'(//a[@href="//www.bilibili.com/anime/"])[2]').is_enabled()
    #检查元素是否可被选中
    #a = driver.find_element(By.XPATH,'(//a[@href="//www.bilibili.com/anime/"])[2]').is_selected()
    print(a)
    sleep(2)
    driver.close()

if __name__ == '__main__':
    test_is_displayed()

