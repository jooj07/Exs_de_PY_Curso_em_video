#contagem regressiva de 10 a 0 com pausa de 1 segundo
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
print('BUUM, BUUM, POW')