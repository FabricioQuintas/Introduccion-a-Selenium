import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo.onestepcheckout.com/')

    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_class_name('q') # Find the search field
        search_field.clear() # Clear search_field

        search_field.send_keys('tee') # Search 'tee' on search field
        search_field.submit() # Submit package

        driver.find_element_by_class_name('link-compare').click() # Add an element to compare
        driver.find_element_by_link_text('Clear All').click() # Clear comparation list

        alert = driver.swith_to.alert # Change to the web alert
        alert_text = alert.text # Take his text

        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
        alert.accept # Accept that alert

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity = 2)