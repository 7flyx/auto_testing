# unittest框架
from selenium import webdriver
import unittest
import time

# 写一个类，继承unittest.Testcase，用于执行测试用例
# 有测试固件，setUp() 做准备工作。tearDown（） 做收尾工作
class Test8(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.url = "https://www.baidu.com/"
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    # 必须以 test_ 作为开头，不然不会被执行
    def test_baidu(self):
        dr = self.driver
        url = self.url
        dr.get(url)
        dr.find_element_by_id("kw").send_keys("许嵩")
        dr.find_element_by_id("su").click()
        time.sleep(3)

    # @unittest.skip("skipping") # 忽略这个测试用例，也就是不执行这个函数
    def test_abaidu(self):
        dr = self.driver
        url = self.url
        dr.get(url)
        dr.find_element_by_id("kw").send_keys("刘翔")
        dr.find_element_by_id("su").click()
        dr.implicitly_wait(5)
        time.sleep(5)
        title = dr.title
        self.assertEqual("刘翔_百度搜索", title, "姓名不对")
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()
