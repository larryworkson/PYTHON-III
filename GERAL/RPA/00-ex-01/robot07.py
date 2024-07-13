from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as p
import pandas as pd


def baixar_plan():
    #baixando planilha
    driver = webdriver.Chrome()
    driver.get('https://rpachallenge.com/assets/downloadFiles/challenge.xlsx')
    p.sleep(3)
    return 'Dados baixados com sucesso!'


def busca_last_name():
    #abrindo o site e identificando o campo ÚLTIMO NOME
    driver = webdriver.Chrome()
    driver.get('https://rpachallenge.com/')
    elemento = driver.find_element(By.XPATH, '//label[text()="Last Name"]')
    txt = elemento.text
    driver.quit()
    return txt

def banco_dados():
    dados = pd.read_excel('"C:\Users\studi\Downloads\challenge.xlsx"', sheet_name='Sheet1')
    df = pd.DataFrame(dados, columns=['First Name', 'Last Name ', 'Company Name', 'Role in Company', 'Address', 'Email', 'Phone Number'])



#'https://rpachallenge.com/'
#   python robot07.py