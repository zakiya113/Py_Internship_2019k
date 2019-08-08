from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Internship_2019\\drivers\\chromedriver.exe")

driver.get("http://www.amazon.in")
driver.maximize_window()
driver.implicitly_wait(10)

ele=driver.find_element_by_xpath("//a[@id='nav-link-accountList']")
hover = ActionChains(driver).move_to_element(ele)
hover.perform()
driver.implicitly_wait(20)

driver.find_element_by_xpath(".//*[@id='nav-flyout-ya-signin']/a/span").click()

# driver.quit()
