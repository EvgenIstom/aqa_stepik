from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    x = (browser.find_element(By.ID, "input_value")).text
    result = math.log(abs(12*math.sin(int(x))))

    input = browser.find_element(By.ID, "answer")
    input.send_keys(str(result))

    browser.execute_script("window.scrollBy(0, 100);")

    button = browser.find_element(By.TAG_NAME, "button")

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button.click()

finally:
    time.sleep(5)
    browser.quit()