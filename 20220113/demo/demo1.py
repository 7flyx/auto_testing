# 定位元素
from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get("https://www.baidu.com/")

# 定位页面的元素--id
# driver.find_element_by_id("kw").send_keys("彭于晏")
# driver.find_element_by_id("su").click()

# xpath-定位元素//*[@id="kw"]
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("彭于晏")
# driver.find_element_by_xpath("//*[@id='su']").click()

# link text---定位页面内唯一的关键字，且是条链接
# driver.find_element_by_link_text("新闻").click()

# partial link text ----跟上诉差不多，只是这个可以补齐部分关键字
# driver.find_element_by_partial_link_text("闻").click()

# css selector -- 也是右击复制 selector
driver.find_element_by_css_selector("#kw").send_keys("彭于晏")
driver.find_element_by_css_selector("#su").submit() # submit 类似于click，但是submit是提交表单的意思

time.sleep(5)

driver.quit()
# driver.close() 二者都是差不多的，但是quit()~会自动清除产生的缓存