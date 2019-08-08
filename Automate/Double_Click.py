from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Internship_2019\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(3)
driver.get('http://only-testing-blog.blogspot.in/2014/09/selectable.html')
driver.implicitly_wait(1)

element = driver.find_element_by_xpath("//button[contains(text(),'Double-Click Me To See Alert')]").click()

driver.implicitly_wait(10)

act = ActionChains(driver)

act.double_click(element).perform()

# driver.switch_to.alert.accept()