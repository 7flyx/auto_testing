# title 和 url
from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get("https://www.baidu.com/")
title = driver.title
print(title)
time.sleep(3)

# 定位元素
driver.find_element_by_id("kw").send_keys("彭于晏")
driver.find_element_by_id("su").click()

url = driver.current_url
print(url)
time.sleep(3)

driver.quit()



