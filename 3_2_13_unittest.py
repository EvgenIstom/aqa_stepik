from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import unittest

chrome_options = Options()
chrome_options.add_argument("--headless")

class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome(options=chrome_options)
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, "[class='form-control first']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "[class='form-control second']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "[class='form-control third']")
        input3.send_keys("mail@mail.net")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Wrong welcome text")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome(options=chrome_options)
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, "[class='form-control first']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "[class='form-control second']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "[class='form-control third']")
        input3.send_keys("mail@mail.net")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Wrong welcome text")


if __name__ == "__main__":
    unittest.main()

