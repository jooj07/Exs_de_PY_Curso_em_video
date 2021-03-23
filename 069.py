"""
Crie um programa que leia idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer
ou não continuar. No final mostre:

a - quantas pessoas tem mais de 18 anos.
b- quantos HOMENS foram cadastrados.
quantas MULHERES têm menos de 20 anos.
"""
hom = dezoito = M20 = 0
while True:
    print('--' * 10)
    print('Cadastro de pessoas')
    print('--' * 10)
    idade = int(input('Idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        dezoito += 1
    if sex == 'M':
        hom += 1
    if sex == 'F' and idade < 20:
        M20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'pessoas com mais de dezoito anos: [{dezoito}]')
print(f'{hom} homens foram cadastrados')
print(f'{M20} mulheres com menos de 20 anos foram castradas')
