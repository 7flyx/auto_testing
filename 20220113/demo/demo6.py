# 鼠标事件
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains # 导入鼠标所需要的包

driver = webdriver.Edge()
driver.get("https://www.baidu.com/")
driver.maximize_window()
# 定位元素，在搜索框输入数据
driver.find_element_by_id("kw").send_keys("赛尔号")
# 点击百度一下按钮
btn = driver.find_element_by_id("su")
ActionChains(driver).context_click(btn).perform() # 右击
time.sleep(2)
ActionChains(driver).double_click(btn).perform() # 双击


time.sleep(2)
driver.quit()