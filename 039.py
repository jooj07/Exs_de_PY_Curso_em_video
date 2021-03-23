'''
Ler o ano do nascimento de um jovem e dizer de acordo com a sua idade:
- se ele ainda vai ter q se alistar
- se é hora de se alistar
- se ja passou da hora
o programa deverá dizer tmb quanto tempo falta para se alistar ou quanto tempo passou
'''

from datetime import datetime
now = datetime.now()
print(now.year)
ano_atual = now.year
nasc = int(input('Em qual ano você nasceu'))
idade = ano_atual - nasc
print(idade)

#caso esteja na hora
if idade == 18:
    print('Poxa que pena está na hora de se alistar')
#caso a idade esteja abaixo dos 18
elif idade < 18:
    print(f'Ainda não está na hora, faltam {18 - idade} anos para você se alistar')
#caso tenha passado do tempo
elif idade > 18:
    print(f'Passou da hora de se alistar hein, você está atrasado em {idade - 18} anos')
