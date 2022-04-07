# -*- coding: UTF-8 -*-
# @Time : 2022/4/7 15:14
# @File : register_page.py
# @Software : PyCharm
import sys
sys.path.append(r"D:\PycharmProjects\SeleniumPyProjectTest\selenium_py_bdd\features\lib")
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class RegisterPage(BasePage):
    def __init__(self, contet):
        super(RegisterPage, self).__init__(contet.driver)

    def send_useremail(self, useremail):
        self.find_element(By.ID, 'register_email').send_keys(useremail)
    def send_username(self, username):
        self.find_element(By.ID, 'register_nickname').send_keys(username)
    def send_password(self, passoword):
        self.find_element(By.ID, 'register_password').send_keys(passoword)
    def send_code(self, code):
        self.find_element(By.ID, 'captcha_code').send_keys(code)
    def click_register_button(self):
        self.find_element(By.ID, 'register-btn').click()
    def get_code_text(self):
        return self.find_element(By.ID, 'captcha_code-error').text
