import unittest
import logging
from appium import webdriver
from configparser import ConfigParser
from appium.webdriver.appium_service import AppiumService
from App.AmazonAppDemo.CartAndBuyotPages import CartAndBuyoutPages
from App.AmazonAppDemo.LoginPage import LoginPage
from App.AmazonAppDemo.ProductPage import ProductPage
from App.AmazonAppDemo.SearchPage import SearchPage


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logging.basicConfig(filename="./logFile.log", filemode="w", format="%(message)s", level=logging.INFO)
        logging.info("Setting Up Appium Desired capabilities and making instance of driver")
        self.config = ConfigParser()
        self.config.read("./Config.cfg")
        self.desCaps = {"platformName": self.config.get("Mobile1", "platformName"),
                        "deviceName": self.config.get("Mobile1", "deviceName"),
                        "platformVersion": self.config.get("Mobile1", "platformVersion"),
                        "udid": self.config.get("Mobile1", "udid"),
                        "automationName": "uiautomator2",
                        "autoWebviewTimeout": 3000,
                        "newCommandTimeout": 14400,
                        'autoAcceptAlerts': True,
                        "autoGrantPermissions": True,
                        "systemPort": 8200,
                        "noReset": False,
                        "appPackage": self.config.get("Mobile1", "appPackage"),
                        "appActivity": self.config.get("Mobile1", "appActivity")}
        self.appium_service = AppiumService()
        self.appium_service.start()
        self.driver = webdriver.Remote(self.config.get("Server", "server"), self.desCaps, keep_alive=False)
        self.driver.implicitly_wait(15)

    def test_login(self):
        """Invoking the login page and signIn the amazon app and fill the otp"""
        logging("Invoking the login page and signIn the amazon app and fill the otp")
        login = LoginPage(self.driver)
        login.signIn()
        login.fillOTP()

    def test_search(self):
        """Searching the item mentioned in the config file and going to list of products"""
        search = SearchPage(self.driver)
        search.searchProduct(self.config.get("SearchProduct", "product"))
        search.selectingItem()

    def test_product(self):
        product = ProductPage(self.driver)
        productDescription, finalRs = product.gatherProductInfo()
        product.addToCart()
        return productDescription, finalRs

    def test_cart(self):
        cart = CartAndBuyoutPages(self.driver)
        prodDescCart, priceDescCart = cart.fetchingProductDetailsFromCart()
        cart.finalBuyout()
        productDescription, finalRs = self.test_product()
        assert finalRs in priceDescCart
        assert prodDescCart[:-3] in productDescription

    @classmethod
    def tearDownClass(self):
        logging.info("Stopping the server and closing the instance of drivers")
        self.driver.close()
        self.driver.quit()
        self.appium_service.stop()


if __name__ == '__main__':
    unittest.main()
