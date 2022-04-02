# -*- coding: UTF-8 -*-
# @Time : 2022/4/2 9:47
# @File : register_function.py
# @Software : PyCharm
import sys
sys.path.append('SeleniumPyProjectTest')
import base64
import time
from PIL import Image
import random
from ShowapiRequest import ShowapiRequest
from selenium import webdriver
from find_element import FindElement

class RegisterFunction(object):
    def __init__(self, url, i):
        self.driver = self.get_driver(url, i)

    def get_driver(self, url, i):
        if i == 0:
            self.driver = webdriver.Chrome()
        elif i == 1:
            self.drvier = webdriver.Edge()
        else:
            self.drvier = webdriver.Firefox()
        self.driver.get(url)
        self.driver.maximize_window()
        return self.driver

    # 输入用户信息
    def send_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)

    # 定位用户信息，获取element
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    # 获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyz', 8))
        return user_info

    # 获取图片
    def get_code_image(self, filename):
        self.driver.save_screenshot(filename)
        code_element = self.get_user_element("code_image")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(filename)
        img = im.crop((left, top, right, height))
        img.save(filename)

    # 解析图片获取验证码
    def code_online(self, filename):
        self.get_code_image(filename)
        with open(filename, 'rb') as fp:
            image_base64 = str(base64.b64encode(fp.read()), encoding='utf-8')
        r = ShowapiRequest("http://route.showapi.com/2360-2", "904965", "ef5258484b1b49e68ce675b72b97a923")
        r.addBodyPara("file_base64", image_base64)
        res = r.post()
        # print(res.text) # 返回信息
        text = res.json()['showapi_res_body']['pic_str']
        return text


    def main(self, i):
        user_name_info = self.get_range_user()
        user_email = user_name_info + "@163.com"
        file_name = "./test02.png"
        #code_text = self.code_online(file_name)
        self.send_user_info('user_email', user_email)
        self.send_user_info('user_name', user_name_info)
        self.send_user_info('user_password', '1111111')
        self.send_user_info('code_text', '11111')
        self.get_user_element('register_button').click()
        code_error = self.get_user_element('code_text_error')
        if code_error == None:
            print('注册成功')
        else:
            self.driver.save_screenshot('./code_error_'+str(i)+'.png')
        time.sleep(5)
        self.driver.close()
        time.sleep(5)

if __name__ == '__main__':
    for i in range(2):
        register_function = RegisterFunction("http://www.5itest.cn/register", i)
        register_function.main(i)