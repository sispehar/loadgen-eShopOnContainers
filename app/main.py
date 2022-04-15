from random import choice
from time import sleep
import sys

from selenium import webdriver
from user import User
from config import Config
from scenarios.scenario import Scenario
from scenarios.scenario_helper import short_sleep
from drivers.chrome_driver_factory import driver_options


def main():
    print("Setting up...")
    user = User()
    options = driver_options(Config.BINARY_PATH)
    while True:
        with webdriver.Chrome(Config.DRIVER_PATH, options=options) as driver:
            user.driver = driver
            driver.get(Config.ESHOP_URL)
            
            if not user.registered:
                user.register()

            user.login()

            s = Scenario(driver)
            try:
                s.start(user)
            except Exception as e:
                print(e)

        print("Scenario finished")
        short_sleep()


if __name__ == '__main__':
    main()
