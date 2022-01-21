

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Edge()
driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("胡歌")
p = driver.find_element_by_id("su") # 定位到 百度一下按钮
ActionChains(driver).double_click(p).perform()

time.sleep(6)

driver.quit()


