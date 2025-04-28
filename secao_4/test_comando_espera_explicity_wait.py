import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Edge()

browser.maximize_window()
browser.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver/")

wait = WebDriverWait(browser, 30) #Espera no máximo 30 segundos para encontrar o elemento

# Usando alert is present
browser.find_element(By.ID, "alert").click() #Encontra o elemento e clica nele
wait.until(EC.alert_is_present()) #Espera até que o alerta seja apresentado
target_alert = browser.find_element(By.ID, "alert").text #Encontra o elemento
assert target_alert == "I am an alert box!", "Alerta não apresentado no elemento"
assert "I am an alert box!" in target_alert, "Alerta não apresentado no elemento"
time.sleep(2)

# Usando text to be present
browser.find_element(By.ID, "populate-text").click() #Encontra o elemento e clica nele
wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*[@class='target-text]"), "Selenium Webdriver")) #Espera até que o texto seja apresentado no elemento
target_text = browser.find_element(By.XPATH, "//*[@class='target-text']").text #Encontra o elemento
assert target_text == "Selenium Webdriver", "Texto não apresentado no elemento"
assert "Selenium Webdriver" in target_text, "Texto não apresentado no elemento"
time.sleep(2)

# Usando element to be clickable
browser.find_element(By.ID, "display-other-button").click() #Encontra o elemento e clica nele
wait.until(EC.element_to_be_clickable((By.ID, "hidden")))
time.sleep(2)

browser.find_element(By.ID, "enable-button").click() #Encontra o elemento e clica nele
wait.until(EC.element_to_be_clickable((By.ID, "disable")))
time.sleep(2)

# Usando element to be selected
checkbox = browser.find_element(By.ID, "ch") #Encontra o elemento
browser.find_element(By.ID, "checkbox").click() #Encontra o elemento e clica nele
wait.until(EC.element_located_to_be_selected(checkbox))
time.sleep(2)

browser.quit()
