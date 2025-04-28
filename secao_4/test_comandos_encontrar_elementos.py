import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()

browser.maximize_window()

browser.get('https://saucedemo.com/')

#Usando o método find_element() para encontrar os elementos
#username = browser.find_element(By.ID, "user-name")
#password = browser.find_element(By.ID, "password")

#Usando send_keys() para preencher os campos
#username.send_keys("standard_user")
#password.send_keys("secret_sauce")

#Usando o método find_elements() para encontrar os elementos
auth_fields = browser.find_elements(By.XPATH, "//input[@class='input_error form_input']")
print("Auth fields:", auth_fields)
print("Tamanho da lista de campos de autenticação:", len(auth_fields))
assert len(auth_fields) == 2, "Número de campos de autenticação inválido"

time.sleep(4)

browser.quit()
