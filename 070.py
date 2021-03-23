"""
Crie um programa q leia o nome e o preço de vários produtos.
O Programa devera perguntar se quer q contuua ou nao

a - qual o total gasto
b - produtos acima de mil
c - o bome do broduto mais barato e preço
"""
maior = menor = total = totmil = cont = 0
barato = ' '
while True:
    print('»»»' * 10)
    print('Loja Olga Romênia Contrabandos LTDA.')
    print('«««' * 10)
    nome = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o preço: R$'))
    cont += 1
    total += valor
    if valor > 1000:
        totmil += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'temos {totmil} produtos que custam mais de R$1000,00')
print(f'O valor da compra foi de: R${total}')
print(f'O produto mais barato foi {barato} e custou R${menor:.2f}')
print('{:-^40}'.format('FIM DO PROGRAMA'))
