"""
Crie um prgrama que tenha uma tupla totalmente preenchida
com uma contagem por extenso, de zero até vinte.
seu programa deverá ler um número pelo teclado de mostrá-lo
por extenso
"""
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
#numero = int(input('Digite um número de zero a vinte: '))
"""if numero in (0, 20):
    print('Você digitou: ', cont[numero])
else:
    print('Número inválido tente novamente')
    numero = int(input('Digite um número de zero a vinte: '))
    print('Você digitou: ', cont[numero])"""
while True:
    numero = int(input('Digite um número de zero a vinte: '))
    if 0 <= numero <=20:
        print(f'Você digitou ({numero}):',cont[numero])
        break
    else:
        print('Você digitou um número inválido, digite novamente.')
