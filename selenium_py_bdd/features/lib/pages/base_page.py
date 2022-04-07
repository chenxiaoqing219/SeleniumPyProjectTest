# -*- coding: UTF-8 -*-
# @Time : 2022/4/7 15:15
# @File : base_page.py
# @Software : PyCharm

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 打开网页
    def get_url(self, url):
        self.driver.get(url)
    # 获取信息
    def get_title(self):
        return self.driver.title
    # 定位元素
    def find_element(self, *loc):
        return self.driver.find_element(*loc)
