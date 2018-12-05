 # encoding: utf-8
import unittest
import login_page
from selenium import webdriver


class TestPythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://the-internet.herokuapp.com/login")

    def test_correct_username(self):
        driver = self.driver
        login = login_page.LoginPage(driver)
        login.login("tomsmith", "SuperSecretPassword!")
        login.assertLoginSuccess(self)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

