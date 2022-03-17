from SeleniumFrameWork.base.DriverClass import WebDriverClass
import time
import SeleniumFrameWork.utilities.CustomLogger as cl
from SeleniumFrameWork.base.BasePage import BaseClass
from SeleniumFrameWork.pages.ContctFormPage import ContactForm

wd= WebDriverClass()
driver=wd.getWebDriver("chrome")
bp=BaseClass(driver)
cf=ContactForm(driver)

bp.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html","Selenium Template")

cf.clickContactForm()
time.sleep(5)
cf.verifyFormPage()
cf.enterName()
cf.enterEmail()
cf.enterMessage()
cf.getCaptha()
cf.enterCaptha()
cf.enterCaptha()
cf.clickOnPostButton()
##ele=bp.getWebElement("user_input","id")
##ele.send_keys("testing")

log = cl.customLogger()
log.info("webpage launched")

time.sleep(2)
driver.quit()