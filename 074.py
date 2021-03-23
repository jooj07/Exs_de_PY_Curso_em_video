'''Crie um programa que vá gerar cinco números aleatórios e colocar em uma tupla
depoois disso, mostre a listagem de números gerados e também indique o menor e maior
número dos que estão na tupla'''
from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os cinco números gerados foram: ')
for n in tupla:
    print(n, end=' ')
print(f'\nO maior valor foi {max(tupla)} e o menor foi {min(tupla)}.')