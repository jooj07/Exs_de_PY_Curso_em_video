'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = str(input('Qual o seu sexo? [F/M]')).upper()[0].strip()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, por favor informe seu sexo: ')).strip().upper()[0]
print(f'{sexo} registrado com sucesso!')
