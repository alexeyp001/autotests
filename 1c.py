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

class Test1с():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
            self.driver.quit()

    def test_1c(self):
        self.driver.get("https://cluster-test.taxcom.ru/")
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element(By.CSS_SELECTOR, ".ylw > a").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".multi .module1__item-order").click()
        self.driver.find_element(By.NAME, "form_text_1243").click()
        self.driver.find_element(By.NAME, "form_text_1243").send_keys("test")
        self.driver.find_element(By.NAME, "form_text_1245").click()
        self.driver.find_element(By.NAME, "form_text_1245").send_keys("1111111111")
        self.driver.find_element(By.NAME, "form_text_1247").click()
        self.driver.find_element(By.NAME, "form_text_1247").send_keys("test@mail.ru")
        self.driver.find_element(By.NAME, "form_text_1249").click()
        self.driver.find_element(By.NAME, "form_text_1249").send_keys("693714798909")
        self.driver.find_element(By.CSS_SELECTOR, "#SIMPLE_FORM_1C_ZAKAZ #submitDemo").click()

