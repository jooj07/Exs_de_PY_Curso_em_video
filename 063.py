#10 primeiros termos da sequencia de fibonacci
#copiei pois não entendi 
Nant = 1
Fibonacci = 0

n = int(input('Digite o número de elementos da sequência: '))

while n != 0:
    print('{}'.format(Fibonacci), end=' → ')
    Fibonacci = Fibonacci + Nant
    Nant = Fibonacci - Nant
    n -= 1
print('FIM')
