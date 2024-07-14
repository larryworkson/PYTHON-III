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


def busca_campo(x):
    #abrindo o site e identificando o campo ÚLTIMO NOME
    driver = webdriver.Chrome()
    driver.get('https://rpachallenge.com/')
    elemento = driver.find_element(By.XPATH, f'//label[text()="{x}"]')
    txt_campo = elemento.text
    driver.quit()
    return txt_campo

def insere_no_campo(lb, dado):
        driver = webdriver.Chrome()
        driver.get('https://rpachallenge.com/')
        label = lb
        atributo_for = label.get_attribute('for')
        inserir = driver.find_element(By.ID, atributo_for)
        inserir.send_keys(dado)
        driver.quit()

def clicar(class_name):
    open = webdriver.Chrome()
    open.get('https://rpachallenge.com/')
    link = open.find_element(By.CLASS_NAME, class_name)
    link.click()


def preencher_form():
    dados = pd.read_excel('C:/Users/studi/Documents/code2024/PYTHON-III/GERAL/RPA/00-ex-01/challenge.xlsx', sheet_name='Sheet1')
    df = pd.DataFrame(dados, columns=['First Name', 'Last Name ', 'Company Name', 'Role in Company', 'Address', 'Email', 'Phone Number'])
    for row in df.itertuples(): # enviando os dados de cada coluna (df) por linha (row)
        label = busca_campo('First Name')
        insere_no_campo(label, row[1]) #ver forma de simplificar o loop
        clicar('uiColorButton')

        


clicar('btn-large')
p.sleep(2)
preencher_form()

#'https://rpachallenge.com/'
#   python robot07.py

'''fazer nova versão sem funções, o webdriver precisa realizar uma única sessão'''