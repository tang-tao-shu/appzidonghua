# -*- coding: utf-8 -*-
# @Time : 2020/12/10 19:08
# @Author : nichao
# @Email : 530504026@qq.com
# @File : case.py
# @Project : page
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from pages.loginpag import LoginPage
from pages.home import HomePage
import unittest
from pages.base_page import BasePage
from model.browser import browser_chrome
from datatool import logindata
from cases.basecase import BaseCase
class MyTest(BaseCase):
    def test_longin_en(self):
        username,password,excepted=logindata()[1]
        driver=browser_chrome()
        lg=LoginPage(self.driver)
        lg.open()
        lg.input_username(username)
        lg.input_password(password)
        lg.input_submit()
        sleep(2)
        hp=HomePage(self.driver)
        self.driver.switch_to.frame('header-frame')
        actual=hp.find_value()
        print(actual)
        #excepted ='退出'
        self.assertEqual(excepted, actual, msg="登陆失败")
        sleep(2)
        # driver.quit()
if __name__=='__main__':
    unittest.main()
