import login_locator

class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver

    def send_username(self, username):
        username_ele = self.driver.find_element(*login_locator.USERNAME_LOCATOR)
        username_ele.send_keys(username)

    def send_password(self, password):
        password_ele = self.driver.find_element(*login_locator.PASSWORD_LOCATOR)
        password_ele.send_keys(password)

    def submit(self):
        button = self.driver.find_element(*login_locator.BUTTON_LOCATOR)
        button.click()

    def login(self, username, password):
        self.send_username(username)
        self.send_password(password)
        self.submit()

    def assertLoginSuccess(self, testcase):
        testcase.assertIn("Secure Area", self.driver.page_source)

