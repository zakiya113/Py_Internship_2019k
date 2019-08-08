from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Internship_2019\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get('https://jqueryui.com/checkboxradio/')
time.sleep(3)

elem = driver.find_element_by_xpath("//a[contains(text(),'Themes')]")
time.sleep(4)
elem.click()
time.sleep(3)
driver.back()
time.sleep(4)
driver.forward()
