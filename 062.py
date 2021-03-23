prim_termo = int(input('Qual o primeiro termo? '))
razao = int(input('E qual a razão? '))
termo = prim_termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end=' → ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Acabou!')
