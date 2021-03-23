'''
Crie uma tupla preenchida com os 10 primeiros colocados da billboard hot 100
e depois mostre:
a - os 5 primeiros
b - os 4 últimos
c - em ordem alfabética
d - em que posição está WAP de Cardi B
'''

hot10 = (
"Franchise", 'Dynamite', 'Wap', 'Laugh Now Cry Later', 'Mood', 'Blinding lights', 'Rockstar', 'Watermelon Sugar',
'I Hope')

cinco_prim = (hot10[0:5])
print('Os cinco primeiros colocados da hot 10 são: ')
for pos, musica in enumerate(cinco_prim,1):
 print(f'{pos}){musica}')

quatro_ultm = (hot10[-4:])
print('\nOs quatro últimos colocados da hot 10 são: ')
for musica in quatro_ultm:
 print(f'{musica}')

print('\nA lista em ordem alfabética: ')
ordem = sorted(hot10)
for pos, ind in enumerate(ordem):
 print(f'{pos}){ind}')

print(f'Wap está na {hot10.index("Wap")+1}ª posição')