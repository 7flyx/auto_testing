# title 和 url 和 浏览器的操作
from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get("https://www.baidu.com/")
title = driver.title
print(title)
time.sleep(3)

# driver.set_window_size(500, 500) # 设置窗口大小
# driver.maximize_window() # 最大化
# driver.minimize_window() # 最小化


# 定位元素
driver.find_element_by_id("kw").send_keys("彭于晏")
driver.find_element_by_id("su").click()

# 浏览器的前进和后退，也就是左上角的两个箭头
# time.sleep(2)
# driver.back() # 后退
# time.sleep(2)
# driver.forward() # 前进

# 右侧滚动条的操作--需要使用到JavaScript
time.sleep(3)
js1 = "var q=document.documentElement.scrollTop=10000" # js语句
driver.execute_script(js1) # 执行js语句
time.sleep(2)


url = driver.current_url
print(url)
time.sleep(3)

driver.quit()



