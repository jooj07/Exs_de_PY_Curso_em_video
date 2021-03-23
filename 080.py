'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
lista = []
for c in range(0, 6):
    valor = int(input("Digite o valor desejado: "))
    lista.append(valor)
    for valor, posi in enumerate(lista):
        print(f'{posi} na posição {valor}')
