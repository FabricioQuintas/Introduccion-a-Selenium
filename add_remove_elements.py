import unittest
from selenium import webdriver
from time import sleep


class AddRemoveElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
        driver = self.driver

        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('How many elements will you add?: '))
        elements_removed = int(input('How many elements will you remove?: '))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')
        sleep(3)

        for _ in range(elements_added):
            add_button.click()

        for _ in range(elements_removed):
            try:
                delete_button = driver.find_element_by_class_name('added-manually')
                delete_button.click()
            except:
                print("You're trying to remove more elements than the existent")
                break
        
        if total_elements > 0:
            print(f'There are {total_elements} elements on screen')
        else:
            print('There are 0 elements on screen')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity = 2)