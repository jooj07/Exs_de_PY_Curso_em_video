'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. '''
lista = []

while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('O valor já existe, digite outro.')
    else:
        lista.append(valor)
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break

lista.sort(reverse=False)
print(f'Você digitou: {lista}')
