from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pyperclip

driver = webdriver.Chrome()
driver.get('https://www.google.com/maps/place/Sal%C3%A3o+Fio+a+Fio/@-27.6724565,-48.6842127,15z/data=!4m11!1m3!2m2!1ssalao+beleza!6e1!3m6!1s0x95273468663e28c3:0xc0a30e0816dd1608!8m2!3d-27.6755925!4d-48.6684515!15sCgxzYWxhbyBiZWxlemGSAQxiZWF1dHlfc2Fsb27gAQA!16s%2Fg%2F11d_84kt6l?entry=ttu')
wait = WebDriverWait(driver, 10)
btn = driver.find_element(By.CSS_SELECTOR, '[data-tooltip="Copiar número de telefone"]')
btn.click()
print(pyperclip.paste())

#       python robot08.py