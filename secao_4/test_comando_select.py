import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
browser.implicitly_wait(12)

browser.maximize_window()
browser.get('https://www.techlistic.com/p/selenium-practice-form.html')

dropdown_continents = Select(browser.find_element(By.XPATH, "//*[@id='continents']"))
dropdown_continents.select_by_visible_text('South America')

time.sleep(3)

browser.quit()
