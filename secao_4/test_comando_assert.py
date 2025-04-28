# O assert sempre verifica se a condição é verdadeira ou falsa
# Se a condição for verdadeira, o código passa
# Se a condição for falsa, o código é interrompido e exibe uma mensagem (opcional)

# Condição verdadeira
"""assert True
assert False, "Condição falsa e código interrompido"
"""

# Usando assert numbers
"""num_esperado = 2
num_obtido = 2

assert num_esperado == num_obtido, f"Número esperado {num_esperado} não é maior que o Número obtido {num_obtido}."
assert num_esperado != num_obtido, f"Número esperado {num_esperado} é igual ao Número obtido {num_obtido}."
"""

# Usando assert text (condição case-sensitive)
"""text_esperado = "Selenium Webdriver"
text_obtido = "Selenium Webdriver"

assert text_esperado == text_obtido, f"Texto esperado {text_esperado} é diferente ao Texto obtido {text_obtido}."
"""

# Usando assert text em string
"""text_esperado = "Selenium Webdriver"
text_obtido = "Webdriver"

assert text_obtido in text_esperado, f"Texto obtido {text_obtido} não contém no Texto esperado {text_esperado}."
"""

# Usando assert com funções is_displayed(), is_enabled(), is_selected()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()

browser.maximize_window()
browser.get("https://www.saucedemo.com/")

username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
button_login = browser.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
button_login.click()
time.sleep(2)

imag_backpack = browser.find_element(By.XPATH, "//img[@alt='Sauce Labs Backpack']")
assert imag_backpack.is_displayed(), "Imagem de backpack nao encontrada"
time.sleep(2)

browser.switch_to.new_window("tab")
browser.get("https://www.techlistic.com/p/selenium-practice-form.html")
gender_male = browser.find_element(By.ID, "sex-0")
assert gender_male.is_enabled(), "Checkbox do gênero masculino nao habilitado"
gender_male.click()
time.sleep(2)

assert gender_male.is_selected(), "Checkbox do gênero masculino nao selecionada"
time.sleep(2)

browser.quit()