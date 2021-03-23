'''ler um número inteiro e
peça para o usuário escolher qual será a base de conversão
1 - para binário
2 - para octal
3 - para hexadecimal
'''
num = int(input('Digite um número de sua escolha: '))
opc = int(input('selecione a base de conversão \n1 - Binário \n2 - Octal \n3 - Hexadecimal \nSelecione:'))
if opc == 1:
    print(f'{num} convertido em binário é igual a: {bin(num)[2:]}')
elif opc == 2:
    print(f'{num} convertido em binário é igual a: {oct(num)[2:]}')
elif opc == 3 :
    print(f'{num} convertido em binário é igual a: {hex(num)[2:]}')
else:
    print('Tente novamente')
