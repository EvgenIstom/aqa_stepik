from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, "input_value").text
    y = str(math.log(abs(12 * math.sin(int(x)))))

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    time.sleep(5)
    browser.quit()