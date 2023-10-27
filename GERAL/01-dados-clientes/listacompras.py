import openpyxl

# Abre a planilha
workbook = openpyxl.load_workbook('E:\Workspace\Drive\Meu Drive\_CODE (drive)\PYTHON\GERAL\01-dados-clientes\comrpas.xlsx')
# Seleciona a planilha a ser trabalhada
worksheet = workbook['Planilha1']

while True:
    print('''[A] = adicionar item
    [B] = Remover item
    [C] = Mostrar lista (soma)
    [S] = Para sair''') 
    m = str(input('Selecione: ')).strip().upper()
    if m == 'A':
        print('Entrou em A')
    if m == 'B':
        print('Entrou em B')
    if m == 'C':
        print('Entrou em C')
    if m == 'S':
        print('Saindo...')
        break
    
