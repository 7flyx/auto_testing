# 操作定位到的元素 --click、submit、clear、text、send_keys
from selenium import webdriver
import time


driver = webdriver.Edge()
driver.get("https://www.baidu.com/")

# clear
# driver.find_element_by_id("kw").send_keys("彭于晏")
# driver.find_element_by_id("su").click()
# time.sleep(2)
# driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys("胡歌")
# driver.find_element_by_id("su").click()
# time.sleep(2)

# text 拿到定位元素的所有文本
text = driver.find_element_by_id("bottom_layer").text
print(text)

time.sleep(4)

driver.quit()




