import logging
from configparser import ConfigParser
import time


class LoginPage():
    _signInnId = "com.amazon.mShop.android.shopping:id/sign_in_button"
    _usrNameXpath = "//android.widget.EditText"
    _continueXpath = "//*[@text='Continue']"
    _passwordXpath = "//android.widget.EditText"
    _submitXpath = "//*[@resource-id='signInSubmit']"
    _continueOTPXpath = "//*[@resource-id='continue']"
    _continueOTPXpath2 = "//*[@text='Continue']"

    def __init__(self, driver):
        self.driver = driver
        self.config = ConfigParser()
        self.config.read("./Config.cfg")

    def signIn(self):
        """Method to Sign in Amazon App using the existing userID and Password from config file"""
        logging.info("Login in using username")
        self.driver.find_element_by_id(self._signInnId).click()
        el1 = self.driver.find_element_by_xpath(self._usrNameXpath)
        el1.send_keys(self.config.get("UserDetails", "usrName"))
        self.driver.find_element_by_xpath(self._continueXpath).click()
        time.sleep(5)
        logging.info("Login in using password")
        el2 = self.driver.find_element_by_xpath(self._passwordXpath)
        el2.send_keys(self.config.get("UserDetails", "password"))
        self.driver.find_element_by_xpath(self._submitXpath).click()
        time.sleep(5)

    def fillOTP(self):
        """otp fills by itslef as phone number in same mobile"""
        logging.info("Otp fills by it self as phone number is in same mobile")
        self.driver.find_element_by_xpath(self._continueOTPXpath).click()
        time.sleep(5)
        logging.info("navigating to search page option")
        self.driver.find_element_by_xpath(self._continueOTPXpath2).click()
