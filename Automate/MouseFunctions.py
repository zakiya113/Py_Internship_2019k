from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Internship_2019\\drivers\\chromedriver.exe")
driver.set_page_load_timeout(20)
driver.get("http://www.theTestingWorld.com/")
driver.maximize_window()
driver.implicitly_wait(10)


act = ActionChains(driver)

# #click Operation
# act.click().perform() #For just clicking wherever the pointer is
# # act.click(driver.find_element_by_xpath("//a[contains(text(),'Login')]")).perform()
#
# #Context Click (right Click)
# act.context_click().perform() #For just right clicking wherever the pointer is
# act.context_click(driver.find_element_by_xpath("//a[contains(text(),'Login')]")).perform()
#
# #Double Click
# act.double_click().perform()
# act.double_click(driver.find_element_by_xpath("//a[contains(text(),'Login')]")).perform()

#Moving control to the required webelement
act.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'TUTORIAL')]")).perform()