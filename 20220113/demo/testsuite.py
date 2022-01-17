# 将所有的测试脚本，集中进行调用
import unittest

import demo.demo7
import demo.demo8


# 搞一个函数，用于返回suite
def getSuite():
    # 1. addTest()--每次只能添加一个脚本里面的一个测试用例
    # suite = unittest.TestSuite()
    # suite.addTest(demo.demo7.Test("test_abaidu"))
    # suite.addTest(demo.demo7.Test("test_baidu"))
    # return suite

    # 2. makeSuite--添加一个类里面的所有测试用例
    # suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(demo.demo7.Test)) # 只需给类名
    # return suite

    # 3. TestLoader--也是可以直接添加一个类里面的所有测试用例--以下两种方法都可以获得测试用例
    suite1 = unittest.TestLoader().loadTestsFromTestCase(demo.demo7.Test)
    suite2 = unittest.defaultTestLoader.loadTestsFromTestCase(demo.demo8.Test8)
    suite = unittest.TestSuite([suite1, suite2])
    return suite

    # 4. discover()--添加的一个包里面的，所有测试脚本的所有测试用例
    # discover = unittest.defaultTestLoader.discover("../demo2", pattern = "demo*.py", top_level_dir=None)
    # return discover

if __name__ == "__main__":
    suite = getSuite()
    runner = unittest.TextTestRunner(verbosity=0)
    runner.run(suite)
