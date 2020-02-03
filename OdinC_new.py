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
import imaplib
import unittest


class OdinC(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://cluster-test.taxcom.ru/')



    def test_1c(self):
        driver = self.driver
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element_by_css_selector(".ylw").click()
        self.driver.execute_script("window.scrollTo(0,500)")
        time.sleep(1)
        self.driver.find_element_by_class_name("module1__item-order").click()
        self.driver.find_element_by_name("form_text_1243").click()
        self.driver.find_element_by_name("form_text_1243").send_keys("test")
        self.driver.find_element_by_name("form_text_1245").click()
        self.driver.find_element_by_name("form_text_1245").send_keys("1111111111")
        self.driver.find_element_by_name("form_text_1247").click()
        self.driver.find_element_by_name("form_text_1247").send_keys("test@mail.ru")
        self.driver.find_element_by_name("form_text_1249").click()
        self.driver.find_element_by_name("form_text_1249").send_keys("221282792714")
        self.driver.find_element_by_css_selector("#SIMPLE_FORM_1C_ZAKAZ #submitDemo").click()
        time.sleep(1)
        assert self.driver.find_element(By.CSS_SELECTOR, ".fancybox-inner > p").text == "Наш менеджер свяжется с Вами в ближайшее время!"
        time.sleep(30)

    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
    unittest.main()


mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
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