"""
faça um programa que jogue para ou impar
o jogo só será interrompido se o jogador perder, mostrando o total
de vitórias q ele conquistou no final do jogo
"""
from random import randint

print('-=' * 20)
print("Vamos jogar par ou impar!")
print('-=' * 20)
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar?[p/i] ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}, total de {total}', end =' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v+=1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você venceu!')
            v+=1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente')
print(f'GAME OVER!, você venceu {v}')
