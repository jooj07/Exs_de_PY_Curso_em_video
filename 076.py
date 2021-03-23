'''Exercício Python 076: Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos preços, na sequência. No final,
mostre uma listagem de preços, organizando os dados em forma tabular.'''
lista = (
    'Lápis', 1.50,
    'Tesoura', 3.57,
    'Estojo Monster High', 26.76,
    'Mochila da Tidinha', 123.56,
    'Caneta', 0.99,
    'Apontador', 1
)
print('-'*50)
print(f'{"Listagem de preços":^50}')
print('-'*50)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>5.2f}')
