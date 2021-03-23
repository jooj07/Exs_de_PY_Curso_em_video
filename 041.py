'''
Leia o ano de nascimento de um atleta e mostre sua categoria
até 9 anos - mirim
ate 14 - infantil
até 19 - junior
até 20 - senior
acima - cacura
'''
from datetime import datetime

now = datetime.now()
print(now.year)
ano_atual = now.year
nasc = int(input('Em qual ano você nasceu'))
idade = ano_atual - nasc

print(f'>>>{idade} anos')

if idade <= 9:
    print('Mirim')
elif idade < 9 or idade <= 14:
    print('infantil')
elif idade < 14 or idade <= 19:
    print('junior')
elif idade < 19 or idade <= 20:
    print('sênior')
else:
    print('Cacura')