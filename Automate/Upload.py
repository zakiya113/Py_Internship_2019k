import time
import os
from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Internship_2019\\drivers\\chromedriver.exe")


driver.get("http://the-internet.herokuapp.com/upload")
time.sleep(5)
driver.find_element_by_id("file-upload").send_keys('E:\\r2.jpg')
time.sleep(5)
driver.find_element_by_id("file-submit").click()

time.sleep(3)