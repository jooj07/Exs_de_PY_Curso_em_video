'''
O programa deve ler 2 números e comparar emitindo uma mensagem que diga:
- o primeiro valor é maior
- ou o segundo valor é maior
- não existe valor maior, os dois são iguais
'''
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

# se 1 for maior que 2
if n1 > n2:
    print('O primeiro valor é maior que o segundo')
# se o 2 for maior que 1
elif n1 < n2:
    print('O segundo valor é maior que o primeiro')
elif n1 == n2:
    print('Os valores são iguais')