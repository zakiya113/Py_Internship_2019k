from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory": "C:\\Users\\minds9\\Desktop\\Py_downloads"})

driver = webdriver.Chrome(executable_path="C:\\Users\\minds9\\PycharmProjects\\Python_Selenium\\drivers\\chromedriver.exe", chrome_options=chromeOptions)

driver.get("http://pypi.python.org/pypi/selenium")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_xpath("//a[@id='files-tab']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[contains(text(),'selenium-3.141.0-py2.py3-none-any.whl')]").click()
















