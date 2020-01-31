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



class elpodpis(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://cluster-test.taxcom.ru')

    def test_elpodpis(self):
        driver = self.driver
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element_by_css_selector(".blue").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(".area1 .col-lg-4:nth-child(2) .tariff-bottom > .btn").click()
        time.sleep(1)
        self.driver.find_element_by_id("byPhone").click()
        self.driver.find_element_by_name("form_text_801").click()
        self.driver.find_element_by_name("form_text_801").send_keys("test")
        self.driver.find_element_by_name("form_text_802").click()
        self.driver.find_element_by_name("form_text_802").send_keys("1111111111")
        self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(15) #submitOtchConnect").click()
        WebDriverWait(self.driver, 5000).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//h2[contains(.,\'Заявка принята!\')]")))
        assert self.driver.find_element(By.CSS_SELECTOR, "h2").text == "Заявка принята!"

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()