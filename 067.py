"""
Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o
número solicitado for negativo
"""
while True:
    resposta = int(input('Digite um número: '))
    if resposta <= -1:
        break
    else:
        for c in range(0, 11):
            resultado = c * resposta
            print(f'{resposta} X {c} = {resultado}')
print('Fim')
