import logging
import time


class CartAndBuyoutPages():
    _prodDescXpath = "//*[@resource-id = 'sc-active-cart']//android.widget.Image/parent::android.view.View/following-sibling::android.view.View/android.view.View"
    _priceDescXpath = "//*[@resource-id = 'sc-active-cart']//android.widget.ListView/android.view.View[1]"
    _navigateAdrsXpath = "//*[@resource-id = 'a-autoid-0-announce']"
    _navigateNextXpath = "//*[@resource-id = 'a-autoid-0-announce']"
    _navigateFinalPaymentXpath = "//*[@text = 'Continue']"

    def __init__(self,driver):
        self.driver = driver

    def fetchingProductDetailsFromCart(self):
        """This method fetches product and price description from Cart page"""
        logging.info("Fetcheing product and price description from Cart page")
        time.sleep(5)
        text1 = self.driver.find_element_by_xpath(self._prodDescXpath).text
        prodDescCart = str(text1)
        text2 = self.driver.find_element_by_xpath(self._priceDescXpath).text
        priceDescCart = text2.encode('utf-8')

        return prodDescCart, priceDescCart

    def finalBuyout(self):
        logging.info("Going to final buyout page")
        self.driver.find_element_by_xpath(self._navigateAdrsXpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self._navigateNextXpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self._navigateFinalPaymentXpath).click()