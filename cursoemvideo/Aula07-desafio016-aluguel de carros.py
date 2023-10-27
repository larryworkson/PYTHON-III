#programa que pergunta a quantidade de km percorridos e a quantidade de dias que o carro foi alugado
#e calcule o preço a pagar. O aluguel do carro custa R$ 60 / dia e R$0,15 por km rodado.
diaria = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos KM rodados? '))
total = (diaria * 60) + (km * 0.15)
print('O total a pagar é: R$ {:.2f}'.format(total))