import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
# By allow to use 2 methods "find_elements" and "find_element"
from selenium.webdriver.common.by import By
# With this we can declare the executable_path of our webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException


class AssertionTest(unittest.TestCase):

    def setUp(self):
        s = Service('C:/chromedriver')  # Route to the webdriver
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver

        driver.get("https://demo.onestepcheckout.com/")
        driver.maximize_window()
        driver.implicitly_wait(5)

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, "q"))

    def tearDown(cls):
        cls.driver.quit()

    def is_element_present(self, how, what):
        '''
        Check if the element is on it
        Args:
        how = selector type
        what = his value
        '''
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True