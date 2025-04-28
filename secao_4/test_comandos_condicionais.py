import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()

browser.maximize_window()

browser.get('https://demo.applitools.com/')

username = browser.find_element(By.ID, "username")
checkbox_remember_me = browser.find_element(By.XPATH, "//*[@type='checkbox']")

#Usando o método is_displayed() para verificar se o campo de usuário está visível
print("O campo de usuário está visível?", username.is_displayed())
assert username.is_displayed(), "O campo de usuário não está visível"

#Usando o método is_enabled() para verificar se o campo de usuário está habilitado
print("O campo de usuário está habilitado?", username.is_enabled())
assert username.is_enabled(), "O campo de usuário não está habilitado"  

#Usando o método is_selected() para verificar se o checkbox de lembrar-me está selecionado
print("O checkbox de lembrar-me está selecionado?", checkbox_remember_me.is_selected())
assert not checkbox_remember_me.is_selected(), "O checkbox de lembrar-me está selecionado"

time.sleep(2)

#Usando o método click() para selecionar o checkbox de lembrar-me
checkbox_remember_me.click()

time.sleep(2)

#Usando o método is_selected() para verificar se o checkbox de lembrar-me está selecionado
print("O checkbox de lembrar-me está selecionado?", checkbox_remember_me.is_selected())
assert checkbox_remember_me.is_selected(), "O checkbox de lembrar-me não está selecionado"

browser.quit()
