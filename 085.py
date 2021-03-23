"""Exercício Python 085: Crie um programa onde o usuário possa digitar
sete valores numéricos e cadastre-os em uma lista
única que mantenha separados os valores pares e ímpares. No final,
mostre os valores pares e ímpares em ordem crescente."""
lista = []
pares = []
impares = []

for c in range (1, 8):
    numero = (int(input(f'Digite o {c}° valor: ')))
    lista.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

pares.sort()
print(f'Os valores pares digitados foram: {pares}')
impares.sort()
print(f'Os valores ímpares digitados foram: {impares}')

