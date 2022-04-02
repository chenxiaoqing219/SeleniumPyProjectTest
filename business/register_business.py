# -*- coding: UTF-8 -*-
# @Time : 2022/4/2 15:41
# @File : register_business.py
# @Software : PyCharm
# 执行层
from handle.register_handle import RegisterHandle
class RegisterBusiness(object):
    def __init__(self):
        self.register = RegisterHandle()
    def register(self, email, name, password, code):
        self.register.send_user_email(email)
        self.register.send_user_name(name)
        self.register.send_user_password(password)
        self.register.send_user_code(code)
        pass