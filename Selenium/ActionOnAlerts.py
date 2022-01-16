from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time


driver = webdriver.Chrome("chromedriver")  # Using Chrome Driver

driver.get("http://www.dummypoint.com/Windows.html")
assert "Selenium Template" in driver.title

wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

wait.until(ec.presence_of_element_located((By.XPATH, '//button[text()="Promt Alert"]'))).click()
time.sleep(2)

# Import Alert class

# Create the object for Alert class
a_button = Alert(driver)


# Using Alert class object call the methods to " 1. accept or 2. dismiss or 3. send text and get text " in Alert box
time.sleep(2)

text_p = a_button.text
print(text_p)

a_button.send_keys("Code2Lead")

a_button.accept()
a_button.dismiss()
a_button.accept()


time.sleep(5)
driver.quit()
