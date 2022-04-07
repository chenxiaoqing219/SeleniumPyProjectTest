# -*- coding: UTF-8 -*-
# @Time : 2022/4/7 14:33
# @File : register_user.py
# @Software : PyCharm
import sys
sys.path.append(r"D:\PycharmProjects\SeleniumPyProjectTest\selenium_py_bdd\features\lib")
from behave import *
#from selenium.webdriver.common.by import By
from pages.register_page import RegisterPage
use_step_matcher('re')

@when('I open the register website "([^"]*)"')
def step_register(context, url):
    RegisterPage(context).get_url(url)
    #context.driver.get(url)
@then('I expect that the title is "([^"]*)"')
def step_register(context, title_name):
    title = RegisterPage(context).get_title()
    assert title_name in title

@when('I set with useremail "([^"]*)"')
def step_register(context, useremail):
    RegisterPage(context).send_useremail(useremail)
@when('I set with username "([^"]*)"')
def step_register(context, username):
    RegisterPage(context).send_username(username)
@when('I set with password "([^"]*)"')
def step_register(context, password):
    RegisterPage(context).send_password(password)
@when('I set with code "([^"]*)"')
def step_register(context, code):
    RegisterPage(context).send_code(code)
@when('I click with registerbutton')
def step_register(context):
    RegisterPage(context).click_register_button()
@then('I expect that text "([^"]*)"')
def step_register(context, code_text):
    text = RegisterPage(context).get_code_text()
    #text = context.driver.find_element(By.ID, "captcha_code-error").text
    assert code_text in text