#nome = str(input('Qual é o seu nome? ')).upper()
#if nome == 'GUSTAVO':
#    print('Que lindo nome você tem!')
#print('Bom dia, {}'.format(nome.capitalize()))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digita a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.2f}'.format(m))
if m >= 7.0:
    print('Parabéns você foi aprovado!')
else:
    print('Que pena, você foi reprovado!')