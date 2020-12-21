# -*- coding: utf-8 -*-
# @Time : 2020/12/14 16:29
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : test_cuxiaobj.py
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
        driver.switch_to.frame("menu-frame")
        sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#menu-ul > li.collapse.lis.ico_2").click()
        driver.find_element(By.CSS_SELECTOR, "#menu-ul > li.explode.lis.ico2_2 > ul > li:nth-child(1) > a").click()
        sleep(2)
        driver.switch_to.parent_frame()
        sleep(2)
        driver.switch_to.frame("main-frame")
        sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#listDiv > table > tbody > tr:nth-child(2) > td:nth-child(8) > a:nth-child(2) > img").click()
        driver.find_element(By.NAME,"snatch_name").send_keys("2324")
        driver.find_element(By.NAME,"keywords").send_keys("2")
        driver.find_element(By.CSS_SELECTOR,"body > div.main-div > form > table > tbody > tr:nth-child(11) > td > input:nth-child(1)").click()
        sleep(5)
        driver.find_element(By.CSS_SELECTOR,"body > div.form-div > form > input[type=text]:nth-child(2)").send_keys("23")
        sleep(5)
        # driver.find_element(By.CSS_SELECTOR, "body > div.form-div > form > input.button").click()
        # sleep(2)
        # driver.find_element(By.CSS_SELECTOR,
        #                     "#listDiv > table > tbody > tr:nth-child(2) > td:nth-child(8) > a:nth-child(3) > img").click()
        # sleep(1)
        # driver.switch_to.alert.dismiss()
        # sleep(1)
        # driver.find_element(By.CSS_SELECTOR,
        #                     "#listDiv > table > tbody > tr:nth-child(2) > td:nth-child(8) > a:nth-child(3) > img").click()
        # sleep(1)
        # driver.switch_to.alert.accept()
        # sleep(1)

    if __name__ == '__main__':
        unittest.main()