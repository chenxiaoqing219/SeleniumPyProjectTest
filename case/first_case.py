# -*- coding: UTF-8 -*-
# @Time : 2022/4/2 15:28
# @File : first_case.py
# @Software : PyCharm
import os
#os.path
import sys
import time

sys.path.append('D:\PycharmProjects\SeleniumPyProjectTest')
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner
from log.user_log import UserLog

class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_name = '..\Images\code.png'
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.driver.maximize_window()
        self.register_b = RegisterBusiness(self.driver)
        self.logger.info("this is chrome")

        #self.file_name = '..\Images\code.png'
    def tearDown(self):
        time.sleep(2)
        #if sys.exc_info()[0]:
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.path.join(os.getcwd(), os.pardir) + '/report/' + case_name + '.png')
                self.driver.save_screenshot(file_path)
        #self.driver.save_screenshot()
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    # 邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息

    def test_register_email_error(self):
        user_email_error = self.register_b.register_email_error('11', 'xiaoxiao01', '111111', self.file_name)
        return self.assertFalse(user_email_error, '测试失败')
    def test_register_username_error(self):
        user_name_error = self.register_b.register_name_error('111@qq.com', 'aa', '111111', self.file_name)
        return self.assertFalse(user_name_error, '测试失败')
    def test_register_password_error(self):
        user_password_error = self.register_b.register_password_error('111211@qq.com', 'xiaoxiao01', '1', self.file_name)
        return self.assertFalse(user_password_error, '测试失败')
    def test_register_code_error(self):
        code_text_error = self.register_b.register_code_error('112211@qq.com', 'xiaoxiao01', '111111', '1111')
        return self.assertFalse(code_text_error, '测试失败')
    def test_register_success(self):
        success = self.register_b.user_base('11111aaa@qq.com', '111aaa', '111111', self.file_name)
        return self.assertFalse(success, '测试成功')
'''
def main():
    first = FirstCase()
    first.test_register_email_error()
    first.test_register_username_error()
    first.test_register_password_error()
    first.test_register_code_error()
    first.test_register_success()
'''
if __name__ == '__main__':
    #unittest.main()
    file_path = os.path.join(os.path.join(os.getcwd(), os.pardir) + '/report/'+'first_case.html')
    fp = open(file_path, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_register_email_error'))
    suite.addTest(FirstCase('test_register_username_error'))
    suite.addTest(FirstCase('test_register_password_error'))
    suite.addTest(FirstCase('test_register_code_error'))
    suite.addTest(FirstCase('test_register_success'))
    #unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="This is first report", description="这是我们第一次测试报告", verbosity=2)
    runner.run(suite)