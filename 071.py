"""
simulador de caixa eletronico
no início pergunte ao usuário qual será o valor a ser sacado
(número inteiro)
o programa vai informar quantas cedulas de cada valor serão entregues

obs:
considere que o caixa possui cédulas
de 50, 20, 10 e 1
"""
valor = int(input('Quanto você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'{totced} de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
