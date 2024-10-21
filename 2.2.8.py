from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

firstname = "Johnny"
lastname = "Eastmond"
email = "johneast@mail.org"
filename = "2.2.8.txt"

values = [firstname, lastname, email, os.path.abspath(filename)]

try:
    browser.get(link)

    for inp, values in zip(browser.find_elements(By.TAG_NAME, "input"), values):
        inp.send_keys(values)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()