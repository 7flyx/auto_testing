# 数据驱动 ddt
import sys
import unittest, csv
import os
from selenium import webdriver
import time
from ddt import ddt, unpack, data, file_data

# 根据传递过来的路径，将文件中的数据加工
def getTxt(file_name):
    # 返回一个二维数组
    res = [] # 开辟一块空间
    path = sys.path[0]
    print(path)
    with open(path + "/resource/" + file_name, 'r', encoding='utf-8') as fp:
        lines = fp.readlines() # 读取全部内容，返回的一个list。每一行，就是一个元素
        i = 0
        for row in lines:
            if i != 0:
                length = len(row)
                index = row.find(',')
                tmp = [row[0:index], row[index + 1:length - 1]] # 左闭右开区间，最后还读取了\n，需要多减去一个
                res.append(tmp)
            i += 1
        return res

@ddt
class TestBaidu(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Edge()
        self.url = "https://www.baidu.com/"
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    @unittest.skip("kipping") # 忽略当前函数
    @data(u"彭于晏", u"胡歌", u"张一山", u"刘翔")
    def test_baidu1(self, value): # 此处的value参数，就是上一行data的数据
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    @unittest.skip("skipping")
    @data([u"彭于晏", u"彭于晏_百度搜索"], [u"胡歌", u"胡歌_百度搜索"],[u"理想", u"刘翔_百度搜索"])
    @unpack # 对上诉数据进行打包，用于下面代码测试
    def test_baidu2(self, first_value, second_value):
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id("kw").send_keys(first_value)
        driver.find_element_by_id("su").click()
        time.sleep(3)
        title = driver.title
        self.assertEqual(second_value, title, msg="与描述不符合")
        # try:
        #     self.assertEqual(second_value, title, msg="与描述不符合")
        # except:
        #     self.get_screen(driver, first_value)

    @data(*getTxt('data.txt'))
    @unpack
    def test_baidu3(self, first_value, second_value):
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id("kw").send_keys(first_value)
        driver.find_element_by_id("su").click()
        time.sleep(3)
        title = driver.title
        self.assertEqual(second_value, title, msg="与描述不符合")

    def get_screen(self, driver, file_name):
        if not os.path.exists("../htmlResult"):
            os.makedirs("../htmlResult")
        nowTime = time.strftime("%Y-%m-%d %H%M%S", time.localtime(time.time()))
        driver.get_screenshot_as_file('../htmlResult/' + nowTime + file_name + '.png')
        time.sleep(1)

if __name__ == "__main__":
    unittest.main()



