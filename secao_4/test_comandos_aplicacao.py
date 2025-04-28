import time

from selenium import webdriver

browser = webdriver.Edge()

browser.get('https://saucedemo.com/')

print("Título da página:", browser.title)

print("URL da página:", browser.current_url)

print("Código HTML da página:", browser.page_source)

browser.quit()
