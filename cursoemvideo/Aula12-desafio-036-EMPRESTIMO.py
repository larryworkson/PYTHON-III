''' programa para aprovar emprestimos. O programa vai perguntar o valor da casa,
o salário do comprador e QUANTOS ANOS ele vai pagar

calcular o valor da prestação mensal, sabendo que ele não pode exceder 30% do salário, se
isto ocorrer o empréstimo será negado'''
import time
print('=' * 35)
print('\033[1;31mSIMULADOR DE EMPRESTIMO IMOBILIÁRIO\033[m')
print('=' * 35)
vc = float(input('Qual o valor da casa? R$ '))
s = float(input('Qual a remuneração? R$ '))
ta = int(input('Quantos anos deseja pagar? '))
p = vc / (ta * 12)

if p > s * 30/100:
    print('...:::AVALIAÇÃO:::...')
    time.sleep(2)
    print('Valor do imóvel: \033[33mR$ {:.2f}\033[m'.format(vc))
    print('Parcela: \033[33mR$ {:.2f}\033[m'.format(p))
    print('Prazo de pagamento: \033[33m{:.0f}x \033[m({:.0f} anos)'.format(ta * 12, ta))
    print('\033[1;34mAnalisando...\033[m')
    time.sleep(2)
    print('Seu empréstimo foi \033[4:31mNEGADO\033[m, pois a parcela compromete mais de 30% do seu salário.')
else:
    print('...:::AVALIAÇÃO:::...')
    time.sleep(2)
    print('Valor do imóvel: \033[33mR$ {:.2f}\033[m'.format(vc))
    print('Parcela: \033[33mR$ {:.2f}\033[m'.format(p))
    print('Prazo de pagamento: \033[33m{:.0f}x \033[m({:.0f} anos)'.format(ta * 12, ta))
    print('\033[1;34mAnalisando...\033[m')
    time.sleep(3)
    print('Seu emprestimo foi \033[1;32mAPROVADO\033[m!')