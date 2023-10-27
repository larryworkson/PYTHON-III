count = 0
s = 0
n = 0
while n != 999:
    n = int(input('Digite um número: '))
    s = s + n
    count = count + 1
    if n == 999:
        s = s - 999
        count = count - 1
print(f'Você inseriu {count} número(s) e a soma total dele(s) é {s}')