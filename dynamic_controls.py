import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicControls(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
        driver = self.driver

        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Dynamic Controls').click()

    def test_dynamic_controls(self):
        driver = self.driver

        checkbox = driver.find_element_by_css_selector('#checkbox > input[type=checkbox]') # Find checkbox by his CSS Selector
        checkbox.click()

        remove_add_button = driver.find_element_by_css_selector('#checkbox-example > button') # Find Remove/Add checkbox by his CSS Selector
        remove_add_button.click()

        WebDriverWait(driver, 15).until( # Wait, as max 15 secs, until
            EC.element_to_be_clickable( # Element can be clickable
                (By.CSS_SELECTOR, '#checkbox-example > button') # This Selector correspond to the Remove/Add button
                )
            )
        enable_disable_button = driver.find_element_by_css_selector('#input-example > button') # Enable/Disable button for text
        enable_disable_button.click()

        WebDriverWait(driver, 15).until( # Wait, as max 15 secs, until
            EC.element_to_be_clickable( # Element can be clickable
                (By.CSS_SELECTOR, '#input-example > button') # This Selector correspond to the Enable/Disable text button
                )
            )
        text_area = driver.find_element_by_css_selector('#input-example > input[type=text]') # Find text field
        text_area.send_keys('Fabri') # Send keys
        
        enable_disable_button.click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity = 2)