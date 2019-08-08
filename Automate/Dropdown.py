from selenium.webdriver.support.select import Select
from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Internship_2019\\drivers\\chromedriver.exe")
driver.set_page_load_timeout(20)
driver.get("http://www.theTestingWorld.com/testings")
time.sleep(1)
driver.maximize_window()

#Enter data into the Textbox
driver.find_element_by_name("fld_username").send_keys("helloworld")
driver.find_element_by_xpath("//input[@placeholder='myusername@gmail.com']").send_keys("testingworldindia@gmail.com")
driver.find_element_by_name("fld_password").send_keys("abcd123")
driver.find_element_by_name("fld_cpassword").send_keys("abcd123")


#Dropdown
#1.Select by Index
obj = Select(driver.find_element_by_name("country"))
obj.select_by_index(1)

#2.Select by Value
# obj.select_by_value("2")

# #3.Select by Visible Text
# obj.select_by_visible_text("Male")
