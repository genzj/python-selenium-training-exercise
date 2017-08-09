# encoding: utf-8

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from time import sleep


class TestPythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://127.0.0.1:8888/dialog-test.html")

    def test_alert_dialog(self):
        driver = self.driver
        self.assertIn(u"Selenium", driver.title)
        elem = driver.find_element_by_id("show-alert")
        elem.click()
        self.assertEqual(u'this is an alert!', driver.switch_to.alert.text)
        driver.switch_to.alert.accept()

    def test_prompt_dialog(self):
        driver = self.driver
        self.assertIn(u"Selenium", driver.title)
        elem = driver.find_element_by_id("show-prompt")
        elem.click()
        self.assertEqual(u'Selenium is great!', driver.switch_to.alert.text)
        driver.switch_to.alert.send_keys('It is great!')
        driver.switch_to.alert.accept()
        out = driver.find_element_by_id('output')
        self.assertEqual('It is great!', out.text)
        elem.click()
        driver.switch_to.alert.dismiss()
        self.assertEqual('Operation aborted.', out.text)

    def tearDown(self):
        for w in self.driver.window_handles:
            self.driver.switch_to.window(w)
            print(self.driver.title)
            self.driver.close()

if __name__ == "__main__":
    unittest.main()