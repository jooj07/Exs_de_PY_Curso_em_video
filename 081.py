'''Exercício Python 081: Crie um programa que vai ler vários números e
colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista = []
while True:
    valor = int(input("Digite seu valor: "))
    lista.append(valor)
    if valor == 5:
        print('Você digitou o valor 5! ')
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if resposta == 'N':
            break
    else:
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if resposta == 'N':
            break
print('Analisando...')
print("-" * 30)
print(f'Aqui está a sua lista: {lista}')
print(f'-' * 10, 'Análise', '-' * 10)

# Quantos valores foram digitados
print(f"Foram digitados: {len(lista)} valores")

# lista decrescente
lista.sort(reverse=True)
print(f"A lista decrescente: {lista}")

# Número 5
if 5 in lista:
    print('Como dito antes, o valor 5 está na lista.')
else:
    print('Você não digitou nenhum valor 5')
