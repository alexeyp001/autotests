from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time



class C1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://cluster-test.taxcom.ru/')



    def test_1c(self):
        self.driver.find_element_by_class_name('col-sm-12 .logo').click()


    def tearDown(self):
            self.driver.quit()

if __name__ == '__main__':
        unittest.main()