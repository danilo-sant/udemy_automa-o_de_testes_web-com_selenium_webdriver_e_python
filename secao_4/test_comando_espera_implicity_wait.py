import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()

#Usando o método implicitly_wait() para esperar um tempo
browser.implicitly_wait(12)

browser.maximize_window()

browser.get('https://chercher.tech/practice/explicit-wait-example/')

check_box = browser.find_element(By.XPATH, "//input[@type='checkbox']")
assert check_box.is_displayed(), "O checkbox não está visível"

time.sleep(3)

print("O checkbox está visível?", check_box.is_displayed())

browser.quit()