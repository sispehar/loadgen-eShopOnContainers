import random
from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def short_sleep():
    sleep(random.randint(1,4))

def long_sleep():
    sleep(random.randint(5,10))

def very_long_sleep():
    sleep(random.randint(15,30))

def wait_element(driver, path):
    try:
        element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, path)),
                f'"{path}" not found'
            )
        return element
    except TimeoutException as e:
        print(e)
        return False
