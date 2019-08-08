from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
driver = webdriver.Firefox(capabilities=cap, executable_path="C:\\path\\to\\geckodriver.exe")

driver.get('http://fb.com')
# driver.quit()
