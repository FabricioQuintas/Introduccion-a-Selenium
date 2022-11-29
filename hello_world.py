import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
# By allow to use 2 methods "find_elements" and "find_element"
from selenium.webdriver.common.by import By
# With this we can declare the executable_path of our webdriver,
# i use chrome but can use it with anyone
from selenium.webdriver.chrome.service import Service


class Search(unittest.TestCase):
    def setUp(self):
        s = Service('C:/chromedriver')  # Route to the webdriver
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver

        driver.get("https://demo.onestepcheckout.com/")
        driver.maximize_window()
        driver.implicitly_wait(5)

    def test_search_text_field(self):
        dsearch_field = self.driver.find_element(By.ID, "search")

    def test_search_by_name(self):
        search_field = self.driver.find_element(By.NAME, "q")

    def test_search_by_class(self):
        self.driver.find_element(By.CLASS_NAME, "input-text")

    def test_search_button(self):
        search_button = self.driver.find_element(By_CLASS_NAME, "search-button")

    def test_search_banner_img(self):
        banner_list = self.driver.find_element(By.CLASS_NAME, "promos")

        banner = banner_list.find_elements(By.TAG_NAME, "img")

    def test_vip_promo(self):
        vip_promo = self.driver.find_element(
            By.XPATH, "//*[@id='top']/body/div/div[2]/div[2]/div/div/div[2]/div/ul/li[4]/a/img")

    def test_icon_cart(self):
        icon_cart = self.driver.find_element(By.CSS_SELECTOR, "div.header-minicart span.icon")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
