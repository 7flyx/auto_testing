# 键盘事件
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 需要导入keys包
import time

driver = webdriver.Edge()
driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("彭于晏")
driver.find_element_by_id("su").submit()
time.sleep(2)
# 要想使用键盘，首先需要定位到某个元素，也就是光标的聚焦
# driver.find_element_by_id("kw").send_keys(Keys.ENTER) # 在输入框点击回车键

# 键盘的组合键
# 将上诉输入的内容进行剪切，然后重新输入新的内容
# 首先还是需要先定位到元素
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
time.sleep(3)

# 重新输入新的数据
driver.find_element_by_id("kw").send_keys("胡歌")
driver.find_element_by_id("kw").send_keys(Keys.ENTER)

time.sleep(3)
driver.quit()
