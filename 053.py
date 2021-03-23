'''
Crie uma programa que leia uma frase qualquer
e diga se ela é um polindromo, desconsiderando os espaços
'''
frase = str(input('Digite uma frase')).strip().upper()
palavras = frase.split()
print(frase)
junto = ''.join(palavras)
#print(f'Você digitoi a frase {junto}')
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
#print(inverso)
if inverso == junto:
    print(f'{inverso} = {junto}')
    print('São palindromos')
else:
    print(f'{inverso} não é igual a: {junto}')
    print('Não são palindromos')