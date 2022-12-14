import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from get_data import * # Import our data reader (in csv)

@ddt
class SearchDDT(unittest.TestCase):
    
    def setUp(self):
        '''
        Add setup of chromedriver, open and maximize an specific webpage (this case, demo-store)
        '''

        self.driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe') # Localize webdriver.exe
        driver = self.driver # Make an alias

        driver.implicitly_wait(30) # Wait 30 seconds until it open
        driver.maximize_window() # Maximize window
        driver.get('http://demo-store.seleniumacademy.com/') # Go to this URL

    @data(*get_data('test_data.csv')) # Get the data from "test_data.csv" to run the test
    @unpack # Unpack it to use in test_search_ddt using it as decorator
    def test_search_ddt(self, search_value, expected_count):
        '''
        Search a product in the web, and count how many products for that type shows.

        Args:
        search_value(any) = This is what we will look for in the webpage browser
        expected_count(int) = How many items must web display for the searched value
        '''
        driver = self.driver # Make an alias for self.driver

        search_field = driver.find_element_by_name('q') # Find element by his name "q", this is the search field
        search_field.clear()
        search_field.send_keys(search_value) # Type what we will look for
        search_field.submit()

        '''
        In the webpage, all products will be shown in a h2 with the class "product-name" on an /a
        With this data we know that any value on it, will be a product that the webpage show to us
        '''
        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        expected_count = int(expected_count) # Make the expected_count an integer

        '''
        If expected_count is higher than 0, it must show products, and must be the same as the expected count
        Else, the webpage will show an message telling that there is no any product to show.

        With this we make 2 asserts that verify this operation
        '''
        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element_by_class_name('note-msg')
            self.assertEqual('Your search returns no results.', message)

        # Print how many products we got
        print(f'Found {len(products)} products.')

    def tearDown(self):
        self.driver.close() # Close the window


if __name__ == '__main__':
    unittest.main(verbosity = 2)