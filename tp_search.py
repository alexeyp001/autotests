import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import unittest

class tp_search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://cluster-test.taxcom.ru')

    def test_tp_search1(self):
        driver = self.driver
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element_by_link_text("Техподдержка").click()
        input_field = driver.find_element_by_id('srchFrm')
        input_field.send_keys('Ветис')
        input_field.send_keys(Keys.ENTER)

        time.sleep(2)

        titles = driver.find_elements_by_tag_name('h4')
        for title in titles:
            assert "Ветис" in title.text.lower()


    def tearDown(self):
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()