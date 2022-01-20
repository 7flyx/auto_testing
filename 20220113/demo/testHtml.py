# html报告生成
import os
import unittest
import time
import HTMLTestRunner

# 得到所有测试用例
import demo.demo9


def createSuite():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(demo.demo9.TestBaidu)
    return suite

if __name__ == "__main__":
    if not os.path.exists("../htmlResult"):
        os.makedirs("../htmlResult")
    now_time = time.strftime("%Y-%m-%d %H%M%S", time.localtime(time.time()))
    file_name = "../htmlResult/" + now_time + ".html"
    with open(file_name, 'wb') as fp:
        # 生成HTMLRunner
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="测试报告",description="用例执行情况")
        suite = createSuite()
        runner.run(suite)
