import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Internship_2019\\drivers\\chromedriver.exe")

driver.get("https://jqueryui.com/draggable/#sortable")
driver.maximize_window()
driver.implicitly_wait(10)

driver.switch_to.frame(driver.find_element_by_css_selector(".demo-frame"))
source = driver.find_element_by_id('draggable')
target = driver.find_element_by_css_selector("#sortable>li:nth-child(3)")

mouse = ActionChains(driver).drag_and_drop(source,target)
mouse.perform()

time.sleep(5)