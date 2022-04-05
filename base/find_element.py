# -*- coding: UTF-8 -*-
# @Time : 2022/4/2 10:32
# @File : find_element.py
# @Software : PyCharm
from selenium.webdriver.common.by import By

from util.read_ini import ReadIni
class FindElement(object):
    def __init__(self, driver):
        self.driver = driver
    def get_element(self, key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element(By.ID, value)
            elif by == 'name':
                return self.driver.find_element(By.NAME, value)
            elif by == 'className':
                return self.driver.find_element(By.CLASS_NAME, value)
            else:
                return self.driver.find_element(By.XPATH, value)
        except:
            self.driver.save_screenshot('../Images/%s.png' %value)
            return None
