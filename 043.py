"""
CALCULADORA DE IMC
- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida

imc = peso/ altura²
"""
print('|-------------------------------------------------------|')
print('+------------------- Cálculo de IMC --------------------+')
print('|-------------------------------------------------------|')
peso = float(input('digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura**2)

print(f'{imc:.2f}')

if imc <= 18.5:
    print('Abaixo do peso')
elif 18.5 < imc <= 25:
    print('Peso ideal')
elif 25 < imc <= 30:
    print('Sobrepeso')
elif 30 < imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')