import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
     command_executor='http://192.168.22.1:4444/wd/hub',
     desired_capabilities=DesiredCapabilities.FIREFOX)

driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("hello")
driver.find_element_by_id("su").click()
time.sleep(2)
driver.close()
