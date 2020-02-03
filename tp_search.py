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

    def test_tp_search(self):
        driver = self.driver
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element_by_link_text("Техподдержка").click()
        self.driver.find_element_by_id("srchFrm").click()
        self.driver.find_element_by_name("").send_keys()

















    def tearDown(self):
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()