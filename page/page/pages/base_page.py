# -*- coding: utf-8 -*-
# @Time : 2020/12/11 15:21
# @Author : nichao
# @Email : 530504026@qq.com
# @File : base_page.py
# @Project : page
from selenium.webdriver.common.by import By
from selenium import webdriver
class BasePage():
    _url = "http://192.168.1.161"

    def __init__(self, driver, url=None):
        self.driver = driver
        if not url:
            url = self._url
        self.url = url
    def open(self):
        self.driver.get(self.url)
    def findelement(self,locator):
        return self.driver.find_element(*locator)
    def findelements(self,locator):
        return self.driver.find_elements(*locator)



