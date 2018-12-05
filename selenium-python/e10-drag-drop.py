# encoding: utf-8

import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains


class TestDragDrop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_draw_square(self):
        width = 200
        driver = self.driver
        # self.driver.get("http://blog.poetries.top/drawing-board/")
        self.driver.get("http://127.0.0.1:8888/")
        self.assertIn(u"drawing-board", driver.title)
        canvas = driver.find_element_by_id('canvas')
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(
            canvas, width / 2, width / 2
        ).click_and_hold().move_by_offset(
            0, width
        ).move_by_offset(
            width, 0
        ).move_by_offset(
            0, -width
        ).move_by_offset(
            -width, 0
        ).release().perform()

if __name__ == "__main__":
    unittest.main()
