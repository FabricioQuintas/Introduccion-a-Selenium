import unittest
from selenium import webdriver


class Tables(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
        driver = self.driver

        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Sortable Data Tables').click()

    def test_sort_tables(self):
        driver = self.driver

        # Get the len of the head data ( Table 1 ), getting a list of elements from his css selector ( -1 for the edit/delete panel )
        columns_size = len(driver.find_elements_by_css_selector('#table1 > thead > tr > th')) - 1
        # Get the len of data size ( in rows ) from the table 1 ( Without header )
        row_size = len(driver.find_elements_by_css_selector('#table1 > tbody > tr'))

        table_data = [[] for i in range(row_size)] # Create a list with empty lists inside (the quantity of rows of the body)
        print(table_data)

        # Lets save all data
        for i in range(row_size): # Iter through each row of the data

            # Now iter through each column of the data
            for j in range(columns_size):
                # Take each head data text of the table
                header_data = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{j + 1}]/span').text # j will iter column by column
                # Take each body data text
                row_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{i + 1}]/td[{j + 1}]').text # i iter row by row
                # Append to the table data, as a dict
                table_data[i].append({header_data : row_data})

        print(table_data)

    def tearDown(self):   
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity = 2)