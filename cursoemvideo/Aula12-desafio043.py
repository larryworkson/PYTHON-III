''' leia o peso e a altura e calcule o IMC e mostre o status de acordo com a tabela:
ABAIXO DE 18.5 = ABAIXO DO PESO
ENTRE 18.5 E 25 = PESO IDEAL
ENTRE 25 E 30 = SOBREPESO
30 ATÉ 40 = OBESIDADE
ACIMA DE 40 = OBESIDADE MORBIDA

imc = peso / altura x altura
(altura deve estar em metros)
'''
p = float(input('Qual seu peso? (Kg) '))
alt = float(input('Qual a sua altura (m)? '))
imc = p / alt ** 2
if imc < 18.5:
    print('Seu IMC é de: {:.1f}'.format(imc))
    print('Você está \033[1;31mABAIXO\033[m do peso ideal.')
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é de {:.2f}'.format(imc))
    print('\033[1;32mPARABÉNS! Você está com o peso ideal!')
elif imc >= 25 and imc < 30:
    print('Cuidado, seu IMC é de {:.1f}'.format(imc))
    print('Você está com \033[1;31mSOBREPESO.\033[m')
elif imc >= 30 and imc < 40:
    print('Seu IMC é de {:.1f}'.format(imc))
    print('Você está com \033[1;31mOBESIDADE.')
else:
    print('Cuidado, seu IMC é de {:.1f}'.format(imc))
    print('Você está com \033[1;31mOBESIDADE MÓRBIDA')

