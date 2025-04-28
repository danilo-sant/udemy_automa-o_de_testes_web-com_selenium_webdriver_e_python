import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()

browser.maximize_window()

browser.get('https://saucedemo.com/')

#Usando o método find_element() para encontrar os elementos
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
button_login = browser.find_element(By.ID, "login-button")

#Usando o método send_keys() para preencher os campos
username.send_keys("standard_user")
password.send_keys("secret_sauce")

#Usando o método sleep() para esperar um tempo
time.sleep(3)

#Usando o método click() para clicar em um botão
button_login.click()

#Usando o método text para obter o texto de um elemento
products_title = browser.find_element(By.XPATH, "//span[@class='title']")
print("Título de produtos:", products_title.text)
assert "Products" in products_title.text, "Título de produtos não encontrado"
assert products_title.text == "Products", "Título de produtos não encontrado"

#Usando o método get_attribute() para obter um atributo de um elemento
imagem_backpack = browser.find_element(By.XPATH, "//img[@alt='Sauce Labs Backpack']")
print("Descrição da imagem:", imagem_backpack.get_attribute("alt"))
assert imagem_backpack.get_attribute("alt") == "Sauce Labs Backpack", "Descrição da imagem não encontrada"
assert "Sauce Labs Backpack" in imagem_backpack.get_attribute("alt"), "Descrição da imagem não encontrada"

browser.quit()
