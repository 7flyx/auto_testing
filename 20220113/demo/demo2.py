# 操作定位到的元素 --click、submit、clear、text、send_keys
from selenium import webdriver
import time

driver = webdriver.Chrome()
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
# text = driver.find_element_by_id("bottom_layer").text
# print(text)
# driver.find_element_by_id("kw").send_keys("彭于晏") # 搜索框 输入彭于晏
# driver.find_element_by_id("su").click() # 点击 百度一下
#
# driver.implicitly_wait(5)
#
# driver.find_element_by_link_text("百度百科").click() # 点击 百度百科，查看详情
# time.sleep(2)

print(driver.title) # 打印title
print(driver.current_url)

driver.maximize_window()
driver.minimize_window()
driver.quit()




