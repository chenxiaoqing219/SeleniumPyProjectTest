# -*- coding: UTF-8 -*-
# @Time : 2022/4/7 14:31
# @File : environment.py
# @Software : PyCharm
from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome()

def after_all(context):
    context.driver.close()