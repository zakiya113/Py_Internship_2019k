from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Internship_2019\\drivers\\chromedriver.exe")
driver.get("http://www.thetestingworld.com/testings/")
driver.maximize_window()
time.sleep(2)

elm = driver.find_element_by_tag_name('html')
elm.send_keys(Keys.PAGE_DOWN)
time.sleep(4)
elm.send_keys(Keys.PAGE_UP)

