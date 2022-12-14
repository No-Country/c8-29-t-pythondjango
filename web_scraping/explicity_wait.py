from handy_wrappers import HandyWrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *
from customlogger import customLogger
from traceback import print_stack
import logging


class ExplicitWaitType:
    log = customLogger(logging.DEBUG)
    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrappers(driver)


    def waitForElement(self, locator, locatorType="id",
                       timeout=0.2, pollFrequency=0.1):
        element = None
        try:
            self.driver.implicitly_wait(0.2)
            byType = self.hw.getByType(locatorType)
            # print(f"Espera maxima :: {timeout} :: hasta que el elemento sea visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,])
            element = wait.until(expected_conditions.visibility_of_element_located((byType, locator)))
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)

        self.driver.implicitly_wait(2)
        return element

    def elementClick(self, element):
        try:
            element.click()
            self.log.info(f"Clicked on element with locator: {element}")

        except:
            self.log.info(f"Cannot click on the element with locator: {element}")
            print_stack()

    def sendKeys(self, data, element):
        try:
            element.send_keys(data)
            self.log.info(f"Sent data on element with locator: {element}" )
        except:
             self.log.info(f"Cannot send data on the element with locator: {element}")


    def get_text(self, element):
        try:
            element.text
            self.log.info(f"Sent data on element with locator: {element}")

        except:
            self.log.info(f"Cannot get text on the element with locator: {element}")
        else:
            return element.text

    def split(self, data, element):
        try:
            element.split(data)
            self.log.info(f"Split realizado correctamente: {element}")

        except:
            self.log.info(f"No se pudo realizar el split: {element}")
        else:
            return element.split(data)

    def int(self, element):
        try:
            int(element)
            self.log.info(f"Int realizado correctamente: {element}")

        except:
            self.log.info(f"No se pudo realizar el int: {element}")
        else:
            return int(element)

    def get_attribute(self, element, attribute):
        try:
            element.get_attribute(attribute)
            self.log.info(f"Attribute get success: {element}")

        except:
            self.log.info(f" cannot get Attribute : {element}")
        else:
            return element.get_attribute(attribute)

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            print("Element not found")
            return False

