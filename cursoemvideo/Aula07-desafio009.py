# escreva um programa que leia um valor em metros e o exiba convertido em centímetros e melímetros
#n1 = float(input('Quantos metros? '))
#c = n1 * 100
#m = c * 10
#print('{} metros é igual à:\n{} cm\n{} mm'.format(n1, c, m))
m = float(input('Digite o valor em metros: '))
dec = m / 10
hec = m / 100
km = m / 1000
dc = m * 10
cm = m * 100
mm = m * 1000
print(m, 'metros corresponde a:')
print(km, 'quilometros')
print(hec, 'hectômetros')
print(dec, 'decâmetros')
print(dc, 'decímetros')
print(cm,'centímetros')
print(mm, 'milimetros')
