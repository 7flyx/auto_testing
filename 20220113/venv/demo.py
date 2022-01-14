from selenium import webdriver
import time

driver = webdriver.Edge()

driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("彭于晏")

driver.find_element_by_id("su").click()

time.sleep(8)

driver.quit()
