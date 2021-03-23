#pedra, papel e tesoura
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura') #0, 1, 2
computador = randint(0,2)
#print(f'O computador escolheu {itens[computador]}')
print('''Suas opçõs:
[0] PEDRA
[1] PAPEL 
[2] TESOURA''')

print('---'*10)
jogador = int(input('Qual é a sua jogada? '))
print('Computador jogou: {}'.format(itens[computador]))
print('Jogador jogou: {}'.format(itens[jogador]))
print('---'*10)

if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('Jogada invalida')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('Jogada invalida')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada invalida')