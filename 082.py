'''Exercício Python 082: Crie um programa que vai ler vários números
e colocar em uma lista. Depois disso, crie duas
listas extras que vão conter apenas os valores pares e os valores
ímpares digitados, respectivamente. Ao final, mostre
o conteúdo das três listas geradas.'''

lista = []
listaPar = []
listaImpar = []
while True:
    valor = int(input('Digite o valor de sua escolha: '))
    lista.append(valor)
    if valor % 2 == 0:
        listaPar.append(valor)
    else:
        listaImpar.append(valor)
    resposta = str(input('Deseja continuar: [S/N]: ')).strip().upper()
    if resposta == 'N':
        break
print('Analisando...')
print("-" * 30)
print(f'Lista completa: {lista}')
print(f'-' * 10, 'Análise', '-' * 10)

print(f'Lista de pares: {listaPar}')

print(f'Lista de ímpares: {listaImpar}')
