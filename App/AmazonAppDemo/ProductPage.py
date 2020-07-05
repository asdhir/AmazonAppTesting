import logging
import time
from appium.webdriver.common import touch_action


class ProductPage():
    _langXpath = "//*[@text = 'English - EN']"
    _langSaveXpath = "//*[@text = 'Save Changes']"
    _prodDescXpath = "//*[@resource-id = 'title_feature_div']//android.view.View"
    _priceDescXpath = "//*[@resource-id = 'atfRedesign_priceblock_priceToPay']//android.widget.EditText"
    _addToCartXpath = "//*[@text = 'Add to Cart']"
    _cartXpath = "com.amazon.mShop.android.shopping:id/action_bar_cart_count"

    def __init__(self, driver):
        self.driver = driver

    def gatherProductInfo(self):
        """Choosing English as default language and fetching the description of the choosen product"""
        logging.info("Choosing English as default language")
        time.sleep(10)
        self.driver.find_element_by_xpath(self._langXpath).click()
        self.driver.find_element_by_xpath(self._langSaveXpath).click()
        logging.info("Fetching the description of the choosen product from product description page")
        txt = self.driver.find_element_by_xpath(self._prodDescXpath).text
        productDescription = str(txt)
        time.sleep(2)
        txt1 = self.driver.find_element_by_xpath(self._priceDescXpath).text
        priceDescription = str(txt1)
        x = priceDescription[6:]
        finalRs = x.strip()

        return productDescription, finalRs

    def addToCart(self):
        """This method scrolls down the Add to cart button ,adds the product to cart and then navigate to cart page"""
        logging.info("Scrolling down the Add to cart button")
        touch = touch_action.TouchAction(self.driver)
        touch.press(x=1031, y=1296).move_to(x=1016, y=487).release().perform()
        touch.press(x=1025, y=1329).move_to(x=1007, y=408).release().perform()
        try:
            self.driver.find_element_by_xpath(self._addToCartXpath).click()
        except:
            touch.press(x=1025, y=1329).move_to(x=1007, y=408).release().perform()
            try:
                self.driver.find_element_by_xpath(self._addToCartXpath).click()
            except:
                raise Exception
        time.sleep(2)
        logging.info("Navigate to cart page")
        self.driver.find_element_by_id(self._cartXpath).click()