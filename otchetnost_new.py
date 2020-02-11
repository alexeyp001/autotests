# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import imaplib


class otchetnost(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://cluster-test.taxcom.ru')


    def test_otchetnost(self):
        driver = self.driver
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element(By.LINK_TEXT, "Отчетность через интернет").click()
        self.driver.execute_script("window.scrollTo(0,2500)")
        self.driver.find_element(By.CSS_SELECTOR, "#col2 a.btn-connect").click()
        self.driver.find_element(By.ID, "byPhone").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "form_text_792").click()
        self.driver.find_element(By.NAME, "form_text_792").send_keys("test")
        self.driver.find_element(By.NAME, "form_text_793").click()
        self.driver.find_element(By.NAME, "form_text_793").send_keys("1111111111")
        self.driver.find_element(By.ID, "submitOtchConnect").click()
        WebDriverWait(self.driver, 5000).until(
          expected_conditions.presence_of_element_located((By.XPATH, "//h2[contains(.,\'Заявка принята!\')]")))
        assert self.driver.find_element(By.CSS_SELECTOR, "h2").text == "Заявка принята!"
        time.sleep(15)


    def teardown_method(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

mail = imaplib.IMAP4_SSL('webmail2.taxcom.ru\owa', 993)
mail.login('alexeyplet00@gmail.com', 'Privet123!')
mail.list()
mail.select('Inbox')

result, data = mail.search(None, '(FROM "support")')

ids = data[0]
id_list = ids.split()
latest_email_id = id_list[-1]

result, data = mail.fetch(latest_email_id, "(RFC822)")
raw_email = data[0][1]
raw_email_string = raw_email.decode('utf-8')
print(raw_email_string)
