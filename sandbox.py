# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# # говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

# s = 'My name is Eugene'
#
# if 'name' in s:
#     print('Substring found')
# else:
#     print('Substring not found')
#
# index = s.find('ene')
# if index != -1:
#     print(f"Substring found at index {index}")
# else:
#     print('Substring not found')



# def test_substring(full_string, substring):
#     if substring not in full_string:
#         print(f'expected "{substring}" to be substring of "{full_string}"')
#
# def test_substring(full_string, substring)

import test_abs_project

print(test_abs1())