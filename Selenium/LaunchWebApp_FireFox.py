from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="./geckodriver")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")

time.sleep(5)
driver.quit()