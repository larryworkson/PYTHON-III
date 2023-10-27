#IMPORTAÇÕES
import random
#time 1 - lakers
t1 = random.randint(60, 130)
nt1 = 'Lakers'

#time 2 - Bulls
t2 = random.randint(60, 130)
nt2 = 'Bulls'


'''sorteio de times
time = (nt1, nt2, nt3, nt4)
srt1 = random.choice(time)
srt2 = random.choice(time)
print(sorteio)'''

#confrontos
#JOGO 1
print('{} {} x {} {}'.format(nt1, t1, t2, nt2))
if t1 > t2:
    print('{} venceu'.format(nt1))
    v1 = nt1
    v2 = nt2
elif t2 > t1:
    print('T2 venceu')
    v1 = nt2
    v2 = nt1

print('''RANKING:
1º - {}
2º - {}'''.format(v1, v2))

