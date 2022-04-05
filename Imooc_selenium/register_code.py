# -*- coding: UTF-8 -*-
# @Time : 2022/4/2 9:20
# @File : register_code.py
# @Software : PyCharm
import base64
import time
from PIL import Image
from selenium.webdriver.common.by import By
import random
from util.ShowapiRequest import ShowapiRequest
from selenium import webdriver
driver = webdriver.Chrome()

# 浏览器初始化
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(5)
# 获取element信息
def get_element(id):
    element = driver.find_element(By.ID, id)
    return element

# 获取随机数
def get_range_user():
    user_info = ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyz', 8))
    return user_info

# 获取图片
def get_code_image(filename):
    driver.save_screenshot(filename)
    code_element = driver.find_element(By.ID, "getcode_num")
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    im = Image.open(filename)
    img = im.crop((left, top, right, height))
    img.save(filename)

# 解析图片获取验证码
def code_online(filename):
    with open(filename, 'rb') as fp:
        image_base64 = str(base64.b64encode(fp.read()), encoding='utf-8')
    r = ShowapiRequest("http://route.showapi.com/2360-2", "904965", "ef5258484b1b49e68ce675b72b97a923")
    r.addBodyPara("file_base64", image_base64)
    res = r.post()
    # print(res.text) # 返回信息
    text = res.json()['showapi_res_body']['pic_str']
    return text

# 运行主程序
def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info+"@163.com"
    file_name = "./test02.png"
    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys("111111")
    get_code_image(file_name)
    text = code_online(file_name)
    get_element("captcha_code").send_keys(text)
    time.sleep(5)
    get_element("register-btn").click()
    driver.close()

run_main()