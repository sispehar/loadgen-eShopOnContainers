from time import sleep
import random

from scenarios.scenario_helper import long_sleep, short_sleep, very_long_sleep
class Scenario:
    def __init__(self, driver):
        self.driver = driver

    def start(self, user):
        short_sleep()
        
        num_items = random.randrange(1, 9)
        print(f"Ordering {num_items} items")
        
        for i in range(num_items):
            catalog = self.driver.find_elements_by_xpath('//form[@action="/Cart/AddToCart"]//input[@type="submit"]')
            item = catalog[random.randrange(1,9)]
            item.click()
            short_sleep()

        ## Checkout
        basket_button = self.driver.find_element_by_xpath('//a[@href="/Cart"]')
        basket_button.click()

        long_sleep()
        print(f"Checkout..")
        checkout_button = self.driver.find_element_by_xpath('//input[@value="[ Checkout ]"]')
        checkout_button.click()
        
        long_sleep()

        continue_shopping_button = self.driver.find_element_by_xpath('//input[@value="[ Place Order ]"]')
        continue_shopping_button.click()
        print(f"Checkout succesful")

        very_long_sleep()
        home = self.driver.find_element_by_xpath('//a[@href="/"]')
        home.click()
        print('returned back Home..')
        
        return True