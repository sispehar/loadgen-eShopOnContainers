from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


class ChromeDriverFactory:
    def __init__(self, driver_path, binary_path, debug):
        self.driver_path = driver_path
        self.binary_path = binary_path
        self.debug = debug
        self.ua = UserAgent(verify_ssl=False)
        
def driver_options(binary_path):
    #ua = UserAgent(use_cache_server=False, verify_ssl=False)
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    # print(f"ua: {ua.random}")
    options = Options()
    options.binary_location = binary_path
    options.headless = True
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--user-agent='{}'".format(ua))
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return options