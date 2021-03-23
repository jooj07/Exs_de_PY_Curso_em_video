l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))

# forma um triangulo?
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os seguimentos podem formar um triângulo do tipo:')
    # Equilátero - todos lados iguais
    if l1 == l2 == l3:
        print('Equilátero')
    # Escaleno - Todos os lados diferentes
    elif l1 != l2 != l3 != l1:
        print('Escaleno')
    # Isósceles - dois lados iguais
    else:
        print('Isósceles')

else:
    print('os seguimentos não formam triângulos')
