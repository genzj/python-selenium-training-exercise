# encoding: utf-8

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestPythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://the-internet.herokuapp.com/login")

    def test_correct_username(self):
        driver = self.driver
        username = driver.find_element_by_name("username")
        username.send_keys("tomsmith")

        password = driver.find_element_by_name("password")
        password.send_keys("SuperSecretPassword!")

        button = driver.find_element_by_tag_name("button")
        button.click()

        self.assertIn("Secure Area", driver.page_source)

    def test_incorrect_username(self):
        driver = self.driver
        username = driver.find_element_by_name("username")
        username.send_keys("test")

        password = driver.find_element_by_name("password")
        password.send_keys("test")

        button = driver.find_element_by_tag_name("button")
        button.click()

        self.assertIn("Your username is invalid!", driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
