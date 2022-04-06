# -*- coding: UTF-8 -*-
# @Time : 2022/4/6 9:40
# @File : first_ddt_case.py
# @Software : PyCharm
import unittest
import ddt
import os
import sys
import time
sys.path.append('D:\PycharmProjects\SeleniumPyProjectTest')
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner
file_name = '..\Images\code.png'
from util.excel_util import ExcelUtil
ex = ExcelUtil()
data = ex.get_data()
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.driver.maximize_window()
        self.register_b = RegisterBusiness(self.driver)
        #self.file_name = '..\Images\code.png'
    def tearDown(self):
        time.sleep(2)
        #if sys.exc_info()[0]:
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                #file_path = os.path.join(os.path.join(os.getcwd(), os.pardir) + '/report/' + case_name + '.png')
                file_path = '../report/'+case_name+'.png'
                self.driver.save_screenshot(file_path)
        #self.driver.save_screenshot()
        self.driver.close()
    '''
    @ddt.data(
        ['12', 'xiaoxiao01', '111111', file_name, 'user_email_error', '请输入有效的电子邮件地址'],
        ['@qq.com', 'xiaoxiao01', '111111', file_name, 'user_email_error', '请输入有效的电子邮件地址'],
        ['334452@qq.com', 'xiaoxiao01', '111111', file_name, 'user_email_error', '请输入有效的电子邮件地址']
    )
    @ddt.unpack
    '''
    @ddt.data(*data)
    def test_register_case(self, data):
        email, username, password, file_name, assertCode, assertText = data
        user_email_error = self.register_b.register_function(email, username, password, file_name, assertCode, assertText)
        self.assertFalse(user_email_error, '测试失败')

if __name__ == '__main__':
    #unittest.main()
    file_path1 = '../report/'+'first_case1.html'
    #file_path = os.path.join(os.path.join(os.getcwd(), os.pardir) + '/report/' + 'first_case1.html')
    fp = open(file_path1, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="This is first report", description="这是我们第一次测试报告",
                                           verbosity=2)
    runner.run(suite)