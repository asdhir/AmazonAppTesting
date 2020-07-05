import logging
import time
from appium.webdriver.common import touch_action


class SearchPage():
    _searchTextId = "com.amazon.mShop.android.shopping:id/rs_search_src_text"
    _searchListXpath = "//*[@resource-id = 'com.amazon.mShop.android.shopping:id/iss_search_dropdown_item_text']"
    _itemXpath = "//*[@resource-id = 'com.amazon.mShop.android.shopping:id/rs_vertical_stack_view']//*[@resource-id = 'com.amazon.mShop.android.shopping:id/list_product_linear_layout']"

    def __init__(self, driver):
        self.driver = driver

    def searchProduct(self, product="65 inch TV"):
        """This method searches for the item in search bar and navigate to next screen where items list is displayed"""
        logging.info("Searching for the item in search bar")
        ele = self.driver.find_element_by_id(self._searchTextId)
        ele.click()
        time.sleep(2)
        ele.send_keys(product)
        logging.info("Navigating to next screen where items list is displayed")
        l = self.driver.find_elements_by_xpath(self._searchListXpath)
        l[0].click()

    def selectingItem(self):
        """This method scrolls down the list of items and chooses an item somewhere near the mid of options available"""
        logging.info("Scrolling down the options")
        time.sleep(5)
        touch = touch_action.TouchAction(self.driver)
        for i in range(3):
            touch.press(x=517, y=1689).move_to(x=534, y=143).release().perform()
            time.sleep(2)
        logging.info("Selecting an item somewhere near the mid of options available")
        ele_list = self.driver.find_elements_by_xpath(self._itemXpath)
        ele_list[2].click()
