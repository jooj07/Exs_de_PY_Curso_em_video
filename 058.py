from random import randint
numsorteado = randint(1, 10)
print('---' * 10)
print('Olá, sou aquele que te observa enquanto você se masturba navegando em: '
      '\nhttps://xvideos.com.br, mais conhecido com Seu Computador! '
      '\nEstou pensando em um número entre 0 e 10, consegue adivinhar qual é?')
print('---' * 10)
jogada = int(input('Qual o seu palpite: '))
cont = 1
while jogada != numsorteado:
    if jogada > numsorteado:
        print('Informe um valor menor...')
    elif jogada < numsorteado:
        print('Informe um valor maior...')
    jogada = int(input('Tente novamente: '))
    cont += 1
print('Parabéns, com {} tentativas você venceu!!!' .format(cont))
