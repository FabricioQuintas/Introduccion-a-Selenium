import unittest
from selenium import webdriver
from api_data_mock import ApiDataMock # our user values


class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo.onestepcheckout.com/')

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a').click() # Press the menu
        driver.implicitly_wait(3)
        driver.find_element_by_link_text('Register').click() # Select "Register" option
        self.assertEqual('Create New Customer Account', driver.title) # Check if we are correctly in create account page

        # Create vars with his paths
        first_name = driver.find_element_by_id('firstname')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button')

        self.assertTrue(
            first_name.is_enabled() 
        and last_name.is_enabled() 
        and email_address.is_enabled() 
        and password.is_enabled() 
        and confirm_password.is_enabled() 
        and submit_button.is_enabled()
        ) # Check if we get all paths correctly

        # Send keys with our Api values
        first_name.send_keys(ApiDataMock.first_name) 
        last_name.send_keys(ApiDataMock.last_name)
        email_address.send_keys(ApiDataMock.email_address)
        password.send_keys(ApiDataMock.password)
        confirm_password.send_keys(ApiDataMock.password)
        submit_button.click()
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity = 2)