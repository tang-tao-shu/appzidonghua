# -*- coding: utf-8 -*-
# @Time : 2020/12/14 17:25
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : test_dingdanyc.py
# @Project : page
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
class MyTest_A(unittest.TestCase):

    def test_a(self):
        driver = webdriver.Chrome()
        sleep(2)
        driver.get("http://192.168.1.161/upload/admin/index.php")
        sleep(2)
        driver.find_element(By.NAME, "username").send_keys("nichao")
        driver.find_element(By.NAME, "password").send_keys("nichao123456")
        driver.find_element(By.CSS_SELECTOR,
                                 "body > form > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(5) > td:nth-child(2) > input").click()
        driver.switch_to.default_content()
        driver.switch_to.frame("menu-frame")
        sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/ul/li[3]").click()
        driver.find_element(By.CSS_SELECTOR, "#menu-ul > li.explode.lis.ico2_3 > ul > li:nth-child(1) > a").click()
        sleep(1)
        driver.switch_to.parent_frame()
        sleep(2)
        driver.switch_to .frame("main-frame")
        sleep(2)
