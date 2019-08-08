from selenium import webdriver
import time
driver = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Internship_2019\\drivers\\chromedriver.exe")

driver.get('http://www.theTestingWorld.com/testings')
driver.maximize_window()
time.sleep(1)

#Fetching Title
print("Title of Page is " + driver.title)

#Fetch URL of Page
print("Page URL is " + driver.current_url)


#Fetch Complete Page HTML
print("******************************************************************************************")
print(driver.page_source)

