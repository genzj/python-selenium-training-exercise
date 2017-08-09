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
        link = driver.find_elements_by_css_selector('#content_left .result .t a')
        self.assertGreater(len(link), 2)
        link[1].click()
        sleep(3)

    def tearDown(self):
        for w in self.driver.window_handles:
            self.driver.switch_to.window(w)
            print(self.driver.title)
            self.driver.close()

if __name__ == "__main__":
    unittest.main()