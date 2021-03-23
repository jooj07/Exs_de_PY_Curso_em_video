'''
Refaça o ex 51, lendo o primeiro termo e a razao de uma PA,
mostrando os 10 priimeiros termos da progressao usando o while
'''

prim_termo = int(input('Qual o primeiro termo? '))
razao = int(input('E qual a razão? '))
termo = prim_termo
cont = 1
while cont <= 10:
    print(f'{termo}', end=' → ')
    termo += razao
    cont += 1
print('Acabou!')
