'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1]> mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:])
    #Para criar cópia tem q fazer um fatiamento total
    temp.clear()
    #para não ficar: [['jooa', 45.7], ['jooa', 45.7, 'jose', 567.9]]
    resp = str(input("Deseja continuar? [S/N] ")).strip().lower()
    if resp == 'n':
        break
print('-'*30)
print(f'Os dados doram: {princ} ')
#print(f'Ao todo foram cadastrados: {len(princ)} pessoas')
print(f'O maior peso foi de: {mai}Kg')
print(f'O menor peso foi de: {men} Kg')
