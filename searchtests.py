import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
# With this we can declare the executable_path of our webdriver
from selenium.webdriver.chrome.service import Service

class SearchTests(unittest.TestCase):

    def setUp(self):
        s = Service('C:/chromedriver')  # Route to the webdriver
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver

        driver.get("https://demo.onestepcheckout.com/")
        driver.maximize_window()
        driver.implicitly_wait(5)
    
    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name("q")
        search_field.clear() # Clean our search field
        search_field.send_keys("tee") # Put this string on the field
        search_field.submit() # Send the package

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name("q")
        search_Field.clear()
        search_field.send_keys("salt shaker")
        search_field.submit()

        # I got his Xpath and save it here
        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')

        # Check if there are 1 only result
        self.assertEqual(1, len(products))

    def tearDown(cls):
        cls.driver.quit()