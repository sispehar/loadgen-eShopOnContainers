from faker import Faker

from scenarios.scenario_helper import wait_element, short_sleep, long_sleep
class User:
    def __init__(self, driver = None):
        fake = Faker()
        self.driver = driver
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.street_address = fake.street_address()
        self.city = fake.city()
        self.state = fake.state()
        self.country = fake.country()
        self.postcode = fake.postcode()
        self.phone_number = fake.phone_number()
        self.card_number = fake.credit_card_number()
        self.cardholder = f'{self.first_name} {self.last_name}'
        self.card_expiry = fake.credit_card_expire()
        self.card_code = fake.credit_card_security_code()
        self.email = fake.free_email()
        self.password = fake.password()
        self.registered = False
    
    def login(self):
        
        try:
            self.driver.find_element_by_xpath(f'//a[@href="/basket"]')
            print(f"{self.email} already logged in...")
        except:
            print(f"logging in...")
        
        login_field = wait_element(self.driver, "//a[@href='/Account/SignIn']")
        if login_field:
            login_field.click()
        else:
            return False
        
        username_field = self.driver.find_element_by_id("Email")
        short_sleep()
        username_field.send_keys(self.email)

        password_field = self.driver.find_element_by_id("Password")
        short_sleep()
        password_field.send_keys(self.password)

        short_sleep()
        
        login_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        
        success = wait_element(self.driver, "//form[@id='logoutForm']")
        if success:
            return True
        else:
            return False
    
    def register(self):
        print(f"registration...")
        short_sleep()
        login_field = wait_element(self.driver, "//a[@href='/Account/SignIn']")
        login_field.click()
        register_button = wait_element(self.driver, "//a[text()='Register as a new user?']")
        register_button.click()
        short_sleep()
        self._send_keys(self.driver.find_element_by_xpath("//input[@id='User_Name']"), self.first_name)
        self._send_keys(self.driver.find_element_by_xpath("//input[@id='User_LastName']"), self.last_name)
        self._send_keys(self.driver.find_element_by_xpath("//input[@id='User_Street']"), self.street_address)
        self._send_keys(self.driver.find_element_by_xpath("//input[@id='User_City']"), self.city)
        self._send_keys(self.driver.find_element_by_xpath("//input[@id='User_State']"), self.state)
        self._send_keys(self.driver.find_element_by_xpath("//input[@id='User_Country']"), self.country)
        self._send_keys(self.driver.find_element_by_xpath("//input[@id='User_ZipCode']"), self.postcode)
        self._send_keys(self.driver.find_element_by_xpath("//input[@id='User_PhoneNumber']"), self.phone_number)
        self._send_keys(self.driver.find_element_by_xpath("//input[@id='User_CardNumber']"), self.card_number)
        self._send_keys(self.driver.find_element_by_xpath("//input[@id='User_CardHolderName']"), self.cardholder)
        self._send_keys(self.driver.find_element_by_xpath("//input[@id='User_Expiration']"), self.card_expiry)
        self._send_keys(self.driver.find_element_by_xpath("//input[@id='User_SecurityNumber']"), self.card_code)
        self._send_keys(self.driver.find_element_by_xpath("//input[@id='Email']"), self.email)
        self._send_keys(self.driver.find_element_by_xpath("//input[@id='Password']"), self.password)
        self._send_keys(self.driver.find_element_by_xpath("//input[@id='ConfirmPassword']"), self.password)

        register_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        register_button.click()
        print(f'registered: u: {self.email} p: {self.password}')
        self.registered = True
        home = self.driver.find_element_by_xpath("//a[starts-with(@href,'/home/ReturnToOriginalApplication')]")
        home.click()
        short_sleep()

        return True
    
    def logout(self):
        logout_button = wait_element(self.driver, "//div[@class='esh-identity']//a[@href='javascript:document.getElementById('logoutForm').submit()']")
        logout_button.click()

    @staticmethod
    def _send_keys(elem, text):
        try:
            elem.send_keys(text)
            short_sleep()
        except Exception as e:
            print(e)

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, driver):
        self._driver = driver