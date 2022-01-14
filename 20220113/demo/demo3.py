# 智能等待
from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("刘翔")
driver.find_element_by_id("su").click()

# time.sleep(5) # 等待页面刷新出来后，点击百度百科
driver.implicitly_wait(5) # 智能等待，页面刷新出来后，直接点击。超过一定时间后，没刷新出来就报异常
driver.find_element_by_link_text("刘翔(国际著名田径运动员、奥运会冠军) - 百度百科").click()

time.sleep(5)

driver.quit()
