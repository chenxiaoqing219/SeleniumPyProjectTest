# -*- coding:utf-8 -*-
import unittest
class FirstCase02(unittest.TestCase):

    def setUp(self) -> None:
        print("这个是case的前置条件")

    def tearDown(self) -> None:
        print("这个是case的后置条件")

    @unittest.skip("不执行第一条")
    def testfirst001(self):
        print("这是第00一条case")
    def testfirst002(self):
        print("这是第00二条case")
    def testfirst003(self):
        print("这是第00三条case")


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase02('testfirst002'))
    suite.addTest(FirstCase02('testfirst001'))
    suite.addTest(FirstCase02('testfirst003'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
