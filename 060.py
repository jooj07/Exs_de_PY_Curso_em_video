'''
Faça um programa que leia um número qualquer e mostre seu fatorial
ex:
5!  = 5x4x3x2x1 = 120
'''

'''modo fácil
print('Modo fácil')
from math import factorial
n = int(input('Digite um número:'))
f = factorial(n)
print(f'o fatorial de {n} é {f}')
'''

n = int(input('Digite um número:'))
c = n
f = 1 #fator nulo de multiplicação é 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end ='')
    f = f * c
    c -= 1
print(f'{f}')
