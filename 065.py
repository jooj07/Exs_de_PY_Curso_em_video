"""
Crie um programa que leia varios números inteiros. No final da execução,
mostre a média entre todos os valores e qual foi o maior e menor valores lidos.
o programa deve perguntar ao usuário se ele quer continuar ou não a digitar os valores.
"""
querounao = 's'
cont = soma = numeros = maior = menor = 0

while querounao in 'Ss':
    numeros = int(input('Digite um número inteiro: '))
    cont += 1
    soma += numeros
    if cont == 1:
        maior = menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        elif numeros < menor:
            menor = numeros
    querounao = str(input('Quer continuar? [s/n] ')).lower().strip()[0]
media = soma/cont
print(f'{cont} digitados, a média entre eles é: {media} ')
print(f'o maior número é {maior} e o menor {menor}')
