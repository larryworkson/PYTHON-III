""" except Exception as erro: #exception vai mostar qual erro
    print('Infelizmente tivemos um problema...')
    print(f'O problema foi {erro.__cause__}') """
try:
    a = int(input('Numero: '))
    b = int(input('Numero: '))
    r = a / b

except (ValueError, TypeError): #erros de valor ou tipo
    print('Tivemos um problema com os tipos de dados inseridos.')
except ZeroDivisionError:
    print('Não é possível dividir o valor por 0.')
except KeyboardInterrupt:
    print('O usuário não inseriu os dados.')
else: #opcional
    print(f'O resultado é {r}')
finally: #aparece sempre, independente do resultado
    print('Volte sempre!')