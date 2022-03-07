from SeleniumFrameWork.base.DriverClass import WebDriverClass
import time
import SeleniumFrameWork.utilities.CustomLogger as cl
from SeleniumFrameWork.base.BasePage import BaseClass

wd= WebDriverClass()
driver=wd.getWebDriver("chrome")
bp=BaseClass(driver)

bp.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html","Selenium Template — DummyPoint")


ele=bp.getWebElement("user_input","id")
ele.send_keys("testing")

log = cl.customLogger()
log.info("webpage launched")

time.sleep(2)
driver.quit()