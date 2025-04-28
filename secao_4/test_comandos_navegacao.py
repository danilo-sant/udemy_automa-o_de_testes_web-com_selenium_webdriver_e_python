import time

from selenium import webdriver

browser = webdriver.Edge()

browser.maximize_window()

browser.get('https://ge.globo.com/')

time.sleep(1)

browser.minimize_window()

time.sleep(1)

browser.maximize_window()

time.sleep(1)

browser.refresh()

time.sleep(1)

browser.get('https://www.saucedemo.com/')

time.sleep(1)

browser.back()

time.sleep(1)

browser.forward()

time.sleep(1)

browser.switch_to.new_window('tab')

browser.get('https://www.google.com/')

time.sleep(1)

browser.switch_to.window(browser.window_handles[0])

time.sleep(1)

browser.close()

time.sleep(3)

browser.switch_to.window(browser.window_handles[0])

browser.switch_to.new_window('tab')

browser.get('https://www.ufrn.br/')

time.sleep(2)

browser.switch_to.new_window('tab')

browser.get('https://www.sti.ufrn.br/')

time.sleep(3)

browser.quit()



