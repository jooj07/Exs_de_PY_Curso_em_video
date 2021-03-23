"""
Crie um programa que leia varios números inteiros pelo teclado.
O programa só vai oarar quando o usuário digitar o valor 999, que é a condição de parada.
no final, mostre quantos números foram digitar e a soma, desconsiderando o flag
"""
numero = cont = soma = 0
while numero != 999:
    numero = int(input('Digite o número desejado [999 para parar] '))
    if numero != 999:
        soma += numero
        cont += 1
print(f'você digitou {cont} números, que somados resultam em: {soma}')
