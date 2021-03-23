# leia um número inteiro e diga se ele é primo ou não
numero = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[1;32m', end=' ')
        tot += 1
    else:
        print('\033[1;31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {numero} foi dividível {tot} vezes')
#fora do laço
if tot == 2:  # se ele foi divisível até 2 vezes, ele é primo
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')
