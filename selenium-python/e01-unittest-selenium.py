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

    def test_search_in_baidu(self):
        driver = self.driver
        driver.get("http://www.baidu.com/")
        self.assertIn(u"百度", driver.title)
        elem = driver.find_element_by_name("wd")
        elem.send_keys("selenium")
        elem.screenshot('x.png')
        elem.send_keys(Keys.RETURN)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'nums'))
        )
        self.assertIn("selenium", driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()