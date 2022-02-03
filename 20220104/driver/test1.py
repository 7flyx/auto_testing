from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("肖战")

driver.find_element_by_id("su").click()

time.sleep(8)

driver.quit()
