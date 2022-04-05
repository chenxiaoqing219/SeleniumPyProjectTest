# -*- coding:utf-8 -*-
import base64

from PIL import Image
from selenium.webdriver.common.by import By
import time
from util.ShowapiRequest import ShowapiRequest
from base.find_element import FindElement
class GetCode:
    def __init__(self, driver):
        self.driver = driver

    # 定位用户信息，获取element
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element
    # 获取图片
    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element("code_image")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)
        time.sleep(3)

    # 解析图片获取验证码
    def code_online(self, file_name):
        self.get_code_image(file_name)
        with open(file_name, 'rb') as fp:
            image_base64 = str(base64.b64encode(fp.read()), encoding='utf-8')
        r = ShowapiRequest("http://route.showapi.com/2360-2", "904965", "ef5258484b1b49e68ce675b72b97a923")
        r.addBodyPara("file_base64", image_base64)
        res = r.post()
        # print(res.text) # 返回信息
        text = res.json()['showapi_res_body']['pic_str']
        return text