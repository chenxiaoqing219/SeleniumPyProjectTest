# -*- coding: UTF-8 -*-
# @Time : 2022/4/1 14:45
# @File : start_browser.py
# @Software : PyCharm
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import random
from PIL import Image

driver = webdriver.Chrome()
#driver = webdriver.Edge()
#driver = webdriver.Firefox()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(3)
print(EC.title_contains("注册"))
driver.save_screenshot("./imooc.png")
code_element = driver.find_element_by_id("getcode_num")
print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open('./imooc.png')
img = im.crop((left, top, right, height))
img.save('./imooc1.png')


'''
#element = driver.find_element_by_class_name("controls")
locator = (By.CLASS_NAME, "controls")
WebDriverWait(driver, 1).until(EC.visibility_of_element_located(locator))
email_element = driver.find_element_by_id("register_email")
print(email_element.get_attribute("placeholder"))
email_element.send_keys("test@163.com")
print(email_element.get_attribute("value"))

for i in range(5):
    user_email = ''.join(random.sample('1234567890abcdefg', 5))+"@163.com"
    print(user_email)
'''
driver.close()
'''
driver.find_element_by_id("register_email").send_keys("xiaoxiao01@qq.com")
user_name_element_node = driver.find_elements_by_class_name("controls")[1]
user_element = user_name_element_node.find_element_by_class_name("form-control")
user_element.send_keys("xiaoxiao01")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("1234")
driver.find_element_by_id("register-btn").click()
'''