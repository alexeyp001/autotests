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



class cto(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://cluster-test.taxcom.ru')

    def test_cto(self):
        driver = self.driver
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element_by_link_text("Онлайн-кассы и обслуживание").click()
        self.driver.find_element_by_xpath("(//a[contains(@href, \'#\')])[6]").click()
        assert self.driver.find_element_by_css_selector(".total_price").text == "15 500"
        self.driver.find_element_by_name("form_text_1069").click()
        self.driver.find_element_by_name("form_text_1069").send_keys("test")
        self.driver.find_element_by_name("form_text_1071").click()
        self.driver.find_element_by_name("form_text_1071").send_keys("1111111111")
        self.driver.find_element_by_id("your-app__submit").click()
        WebDriverWait(self.driver, 5000).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//h2[contains(.,\'Заявка принята!\')]")))
        assert self.driver.find_element(By.CSS_SELECTOR, "h2").text == "Заявка принята!"

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()