lista = []
for c in range(1,6):
    n = int(input(f'Digite o {c}° o valor: '))    
    lista.append(n)
    if len(lista) == 1:
        print('Valor add no final da lista!')
    if len(lista) > 1:       
        for pos in range(0, len(lista)):
            ant = pos - 1
            if n > lista[pos]:
                lista.pop(lista.index(n))
                lista.insert(pos, n)            
                break
            else:
                if n == min(lista):
                    lista.pop(lista.index(n))
                    lista.insert(0, n)
                    break
                else:
                    lista.pop(lista.index(n))
                    lista.insert(ant, n)                
                    break
print(lista)