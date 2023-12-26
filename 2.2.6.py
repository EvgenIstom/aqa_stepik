from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.execute_script("alert('Robots at work');")

finally:
    time.sleep(5)
    browser.quit()