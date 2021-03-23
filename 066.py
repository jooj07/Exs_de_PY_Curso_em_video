"""
Leia vários números e some sem a flag 999
"""
n = cont = soma = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Fim, {cont} números que somados dão: {soma}')