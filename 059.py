print('+-------------------------------------------------------+')
print('|                 Calculadora v3.0                       |')
print('|              new: Agora com funções!                   |')
print('+--------------------------------------------------------+')


def soma():
    print('------------------SOMA------------------')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    print(f"{n1} + {n2} = {n1 + n2:.1f}")


def subt():
    print('------------------SUBTRAÇÃO------------------')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    print(f'{n1} - {n2} = {n1 - n2:.1f}')


def mult():
    print('------------------MULTIPLICAÇÃO------------------')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    print(f'{n1} X {n2} = {n1 * n2:.1f}')


def div():
    print('------------------DIVISÃO------------------')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    print(f'{n1} / {n2} = {n1 / n2:.1f}')


def soma3():
    print('------------------SOMA------------------')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))
    print(f"{n1} + {n2} + {n3} = {n1 + n2 + n3:.1f}")


def subt3():
    print('------------------SUBTRAÇÃO------------------')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))
    print(f'{n1} - {n2} - {n3} = {n1 - n2 - n3:.1f}')


def mult3():
    print('------------------MULTIPLICAÇÃO------------------')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))
    print(f'{n1} X {n2} x {n3} = {(n1 * n2) * n3:.1f}')


def div3():
    print('------------------DIVISÃO------------------')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))
    print(f'({n1} / {n2}) / {n3} = {(n1 / n2) / n3:.1f}')


def soma4():
    print('------------------SOMA------------------')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))
    n4 = float(input('Digite o quarto número: '))
    print(f"{n1} + {n2} + {n3} + {n4}= {n1 + n2 + n3 + n4:.1f}")


def subt4():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))
    n4 = float(input('Digite o quarto número: '))
    print(f'{n1} - {n2} - {n3} - {n4} = {n1 - n2 - n3 - n4:.1f}')


def mult4():
    print('------------------MULTIPLICAÇÃO------------------')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))
    n4 = float(input('Digite o quarto número: '))
    print(f'{n1} X {n2} X {n3} X {n4} = {(n1 * n2) * (n3 * n4):.1f}')


while True:
    escolha = str(input('Deseja fazer uma nova operação? [S/N?] ')).strip().lower()
    if escolha == 'n':
        break
    else:
        numeros = int(input('Com quantos números será feita sua operação? [2, 3 ou 4?] '))

        if numeros == 2:
            operação = str(input(('Qual operação deseja fazer? \n(+) ADIÇÃO \n(-) SUBTRAÇÃO \n(X) MULTIPLICAÇÃO \n(/) '
                                  'DIVISÃO \n=> '))).strip().lower()
            if operação == '+':  # soma com 2 números
                print(soma())

            elif operação == '-':  # subtração com dois números
                print(subt())

            elif operação == 'x':  # multiplicação com dois números
                print(mult())

            elif operação == '/':  # divisão com dois números
                print(div())
        elif numeros == 3:
            operação = str(input(('Qual operação deseja fazer? \n(+) ADIÇÃO \n(-) SUBTRAÇÃO \n(X) MULTIPLICAÇÃO \n(/) '
                                  'DIVISÃO \n=> '))).strip().lower()
            if operação == '+':  # soma com 3 números
                print(soma3())

            elif operação == '-':  # subtração com 3 números
                print(subt3())

            elif operação == 'x':  # multiplicação com 3 números
                print(mult3())

            elif operação == '/':  # divisão com 3 números
                print(div3())
        elif numeros == 4:
            operação = str(input(
                'Qual operação deseja fazer? \n(+) ADIÇÃO \n(-) SUBTRAÇÃO \n(X) MULTIPLICAÇÃO \n=> ')).strip().lower()
            if operação == '+':  # soma com 4 números
                print(soma4())

            elif operação == '-':  # subtração com 4 números
                print(subt4())

            elif operação == 'x':  # multiplicação com 4 números
                print(mult4())
print('Operação finalizada')
