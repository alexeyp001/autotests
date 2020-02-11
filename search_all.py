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

class search_mini(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://cluster-test.taxcom.ru')

    def test_search_mini(self):
        driver = self.driver
        self.driver.set_window_size(1920, 1080)

        search_input = driver.find_element_by_id('srchFrm-mini')

        # Ввод текста
        search_input.send_keys('Цто')
        search_input.submit()

        # Проверка результатов поиска
        search_result = driver.find_elements_by_class_name('search-item')

        assert len(search_result) > 0
        for result in search_result:
            title_text = result.find_element_by_tag_name('h4').text
            desc_text = result.find_element_by_class_name('search-preview').text
            assert title_text.lower().find('цто') != -1 or desc_text.lower().find('цто') != -1


    def tearDown(self):
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()