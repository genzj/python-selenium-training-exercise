# encoding: utf-8

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from time import sleep


class ReactionTime(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_reaction_time(self):
        driver = self.driver
        self.driver.get("http://127.0.0.1:8888/")
        for i in range(5):
            elem = driver.find_element(By.CLASS_NAME, 'button')
            elem.click()
            WebDriverWait(driver, 15, poll_frequency=0.01).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, 'armed')
                )
            )
            elem.click()
            sleep(1)
        result = driver.find_element(By.CLASS_NAME, 'times')
        print(result.text)

if __name__ == "__main__":
    unittest.main()
