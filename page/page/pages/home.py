# -*- coding: utf-8 -*-
# @Time : 2020/12/10 21:53
# @Author : nichao
# @Email : 530504026@qq.com
# @File : home.py
# @Project : page
from selenium.webdriver.common.by import By
from page.pages.base_page import BasePage
class HomePage(BasePage):
    _url = BasePage._url+"/upload/admin/index.php"
    marketing_locator=(By.CSS_SELECTOR,"#submenu-div > ul > li:nth-child(1) > a > span")
    def find_value(self):
        return self.findelement(self.marketing_locator).text
