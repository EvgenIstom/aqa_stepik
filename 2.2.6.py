from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.execute_script("alert('Robots at work');")

finally:
    time.sleep(5)
    browser.quit()