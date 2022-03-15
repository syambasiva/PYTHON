
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time


driver = webdriver.Chrome("chromedriver")  # Using Chrome Driver

driver.get("https://yopmail.com/en/")

time.sleep(20)
##shrawni@yopmail.com
username = (By.XPATH, '(//div[@class="wminboxheader"]/div/button/i[@class="material-icons-outlined"])[1]')
driver.find_element(*username).click()
time.sleep(2)

username1 = (By.XPATH, '//span[text()="Empty Inbox"]')
driver.find_element(*username1).click()
time.sleep(2)

a_button = Alert(driver)

a_button.accept()

time.sleep(5)
driver.quit()
