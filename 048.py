'''
Faça um programa que calcule a soma entre todos os
NÚMEROS IMPARES que são MULTIPLOS DE TRÊS e que se encontram
no intervalo de 1 a 500.
'''
soma = 0  # acumulador
cont = 0  # contador
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        cont += 1
        soma += c
print(f' A soma de todos os {cont} valores socilidatos é de {soma}.')
