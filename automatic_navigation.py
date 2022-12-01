import unittest
from selenium import webdriver
from time import sleep

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo.onestepcheckout.com/')

    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q') # Find search_field by his name: 'q'
        search_field.clear() # Clear search field
        search_field.send_keys('Platzi') # Type: 'Platzi' in search field
        search_field.submit() # Submit

        sleep(3) # Sleep 3 secs
        driver.back() # Go back to the previous page
        sleep(3)
        driver.forward() # Go to the incoming page
        sleep(3)
        driver.refresh() # Refresh web
        
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity = 2)