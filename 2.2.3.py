from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")

    x = num1.text
    y = num2.text

    z = int(x) + int(y)
    print(z)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()


finally:
    time.sleep(5)
    browser.quit()
