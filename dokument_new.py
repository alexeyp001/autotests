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

class dokument(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://cluster-test.taxcom.ru')


    def test_dokument(self):
        driver = self.driver
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element_by_link_text("Электронный документооборот").click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,3200)")
        time.sleep(2)
        self.driver.find_element_by_css_selector(".esp__tariffs__tariff-card:nth-child(3) > .esp__tariffs__tariff-card__button").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".esp__tariffs__tariff-card__price").text == "2 000"
        self.driver.find_element(By.CSS_SELECTOR, ".esp__auto-complete__input-wrapper").click()
        self.driver.find_element(By.CSS_SELECTOR, ".esp__auto-complete__input-wrapper").send_keys("f")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".esp__auto-complete__input-wrapper").send_keys(Keys.DOWN)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".esp__auto-complete__input-wrapper").send_keys(Keys.ENTER)
        self.driver.find_element(By.NAME, "email").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "email").send_keys("test@mail.ru")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".esp__tariffs__request__second-step").click()
        time.sleep(1)
        assert self.driver.find_element(By.CSS_SELECTOR,"div:nth-child(1) > .esp__tariffs__first-form__field-label:nth-child(1)").text == "E-mail test@mail.ru уже зарегистрирован"


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()