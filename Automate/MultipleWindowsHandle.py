from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Internship_2019\\drivers\\chromedriver.exe")
driver.get("https://lms.latitudelearning.com")
driver.maximize_window()

#login
driver.find_element_by_xpath("//input[@id='ctlTemplate_regMainBody_ctlLogin_sID']").send_keys("MANI1")
time.sleep(2)
driver.find_element_by_xpath("//input[@id='ctlTemplate_regMainBody_ctlLogin_sPassword']").send_keys("Minds123")
time.sleep(2)
driver.find_element_by_xpath("//input[@id='ctlTemplate_regMainBody_ctlLogin_cmdLogin']").click()
time.sleep(2)

#Admin link
driver.find_element_by_xpath("//a[@class='header-admin']").click()
time.sleep(2)
#click on course
driver.find_element_by_xpath("//a[@id='ctlTemplate_regLeftNav_ctlMenuUser_mnuUser_MenuSection4_SectionHeader']").click()
time.sleep(2)
#click on add course
driver.find_element_by_xpath("//a[@id='ctlTemplate_regLeftNav_ctlMenuUser_mnuUser_MenuSection4_SectionItemsRepeater_ctl01_SectionItem']").click()

#choose organization
driver.find_element_by_xpath("/html[1]/body[1]/form[1]/div[3]/table[1]/tbody[1]/tr[1]/td[2]/div[2]/div[1]/div[2]/fieldset[1]/div[1]/dl[1]/dd[1]/a[1]").click()

driver.switch_to.window(driver.window_handles[1])

time.sleep(5)
driver.find_element_by_xpath("/html[1]/body[1]/form[1]/div[3]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/div[2]/span[1]/div[2]/div[1]/input[1]").click()
time.sleep(2)
driver.find_element_by_xpath("/html[1]/body[1]/form[1]/div[3]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/table[2]/tbody[1]/tr[2]/td[3]/input[1]").click()
time.sleep(2)
driver.find_element_by_xpath("/html[1]/body[1]/form[1]/div[3]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/input[1]").click()
time.sleep(2)