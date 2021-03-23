"""
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares."""

tupla_num = (int(input('Insíra um número: ')),
             int(input('Insíra um número: ')),
             int(input('Insíra um número: ')),
             int(input('Insíra um número: ')))
c = 0
nove = tupla_num.count(9)
print(tupla_num)

# contador de número par, excluíndo o zero
for n in tupla_num:
    if n != 0 and n % 2 == 0:
        c += 1
#detecta 3
if 3 in tupla_num:
    pos = tupla_num.index(3)
    print(f'O número 3 aparece na posição {pos}')
else:
    print('Você não digitou nenhum 3')

#Diz se tem mais de um número par de forma correta
if c == 0:
    print('Você não digitou nenhum número par')
elif c == 1:
    print('Existe 1 número par na tupla')
else:
    print(f'Nesta tupla há {c} números pares')

#Diz quantaas vezes o número 9 aparece de forma correta
if nove == 0:
    print('Você não digitou nenhum 9.')
elif nove == 1:
    print('Você digitou um número nove.')
else:
    print(f'Você digitou o número 9 » {nove} vezes.')


#print(f'o número 9 aparece: {tupla_num.count(9)} vezes na tupla')
