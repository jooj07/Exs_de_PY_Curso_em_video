'''
O programa deverá ler 6 números inteiros e
mostrar a soma só daqueles que forem pares,
se o valor digitado for impar, desconsidere.
'''
acumulador = 0
for c in range(0, 7):
    numero = int(input('Digite um número inteiro: '))
    print('---' * 10)
    if numero % 2 == 0:
        acumulador += numero
print('-=-' * 10)
print(f'A soma é: {acumulador}')
print('-=-' * 10)
