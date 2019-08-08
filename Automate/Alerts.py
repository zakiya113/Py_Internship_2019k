from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Internship_2019\\drivers\\chromedriver.exe")

driver.get("http://demo.guru99.com/test/delete_customer.php")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_name("cusid").send_keys("53920")
driver.find_element_by_name("submit").click()

driver.switch_to.alert.accept()
time.sleep(2)
driver.switch_to.alert.dismiss()
