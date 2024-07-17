from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pyperclip

""" driver = webdriver.Chrome()
driver.get('https://www.google.com/maps/search/salao+beleza/@-27.6773724,-48.6817139,15z/data=!4m2!2m1!6e1?entry=ttu')
wait = WebDriverWait(driver, 10) """
clicar = webdriver.Chrome()
clicar.get('https://www.google.com/maps/search/salao+beleza/@-27.6773724,-48.6817139,15z/data=!4m2!2m1!6e1?entry=ttu')
links = clicar.find_elements(By.CLASS_NAME, 'hfpxzc')
primeiro_link = links[0]
primeiro_link.click()
wait = WebDriverWait(clicar, 10)
""" btn = clicar.find_elements(By.CLASS_NAME, "AeaXub")
btn.click()
print(pyperclip.paste()) """

#       python robot08.py