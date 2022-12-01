import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import select

class LanguageOptions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo.onestepcheckout.com/')

    def test_select_language(self):
        exp_options = ['English', 'French', 'German'] # This is how they appears on the webpage
        act_options = []

        select_language = Select(self.driver.find_element_by_id('select-language')) # Access to select-language options

        self.assertEqual(3, len(select_language.options)) # Check if its the correct lenght

        for option in select_language.options: # Iterate through select_language
            act_options.append(option.text) # Add the option TEXT

        self.assertListEqual(exp_options, act_options) # Check if both lists are the same

        self.assertEqual('English', select_language.first_selected_option.text) # Check if the first option is 'English'

        select_language.select_by_visible_text('German') # Select 'German' by his visible text
        self.assertTrue('store=german' in self.driver.current_url) # Check if the web changed to German

        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.implicitly_wait(5)
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity = 2)