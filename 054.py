# leia a data de nascimento de 7 pessoas e diga quantas são maiores e quantas não
from datetime import date

ano_atual = date.today()
cont1 = 0  # contador
cont2 = 0
for npessoas in range(0, 8):
    print('---' * 20)
    ano_nasc = int(input('Digite o ano que você nasceu: '))
    print('---' * 20)
    if ano_atual.year - ano_nasc >= 18:
        # print('maior de idade')
        cont1 += 1
    else:
        # print('não é maior de idade')
        cont2 += 1
print(f'{cont1} Pessoas dentre as informadas \033[1;32msão maiores de idade\033[m')
print(f'{cont2} Pessoas dentre as informadas \033[1;31mnão são maiores de idade\033[m')
