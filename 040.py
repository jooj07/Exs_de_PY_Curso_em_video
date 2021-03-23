'''
Um programa que leia duas notas e faça média
aabaixo de 5 - reprovado
entre 5 e 6.9 - recuperação
media acima de 7 - aprovado
'''
n1  = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
md = (n1 + n2) / 2
if md < 5.0:
    print('Reprovado')
elif md == 5.0 or md <= 6.9:
    print('Recuperação')
else:
    print('Aprovado')