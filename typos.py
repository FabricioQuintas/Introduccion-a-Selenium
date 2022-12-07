import unittest
from selenium import webdriver


class Typos(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
        driver = self.driver

        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Typos').click()

    def test_find_typo(self):
        driver = self.driver
        
        correct_text = "Sometimes you'll see a typo, other times you won't." # Correct text that page must show

        paragraph_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)') 
        tries = 1 # Initialize a number of tries

        while correct_text != paragraph_to_check.text: # If correct text isn't equal the paragraph to check
            tries += 1 # Add 1 try
            driver.refresh() # Refresh the page
            paragraph_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)') # Reasign the new text

        if tries == 1:
            print('Typo found at the first try.') # Tries == 1 means first try
        else:
            print(f'It took {tries} tries to find the typo') 

    def tearDown(self):   
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity = 2)