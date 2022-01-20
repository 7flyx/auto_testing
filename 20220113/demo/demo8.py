# unittest框架
from selenium import webdriver
import unittest
import time
import os

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
        try:
            self.assertEqual("刘翔百度搜索", title, "姓名不对")
        except:
            self.screen_shot(dr, "刘翔_百度搜索")
        time.sleep(3)

    # 产生错误，截图保存
    def screen_shot(self, driver, file_name):
        if  not os.path.exists("./image"):
            os.makedirs("./image")
        now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        driver.get_screenshot_as_file('./image/' + now + file_name + ".png") # 获取截图，并存储
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
