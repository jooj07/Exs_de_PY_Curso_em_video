'''
Aprovar empréstimo bancário:
o programa vai perguntar o VALOR DA CASA, o SALÁRIO e em QUANTOS ANOS ele vai pagar
o valor da prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado
'''
valorcasa = float(input('Qual o valor da casa que deseja comprar? R$'))
salr = float(input('Quanto você recebe por mês? R$'))
anos = int(input('Em quantos anos você pretende pagar a casa? '))
prestacao = valorcasa / (anos * 12)
trintslr = salr * 30 / 100
print(f'Para pagar uma casa de {valorcasa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}')
#print(f'COMPARANDO tem que pagar {prestacao} e o mínimo é de {trintslr}')
if prestacao <= trintslr:
    print('Empréstimo aprovado!')
else:
    print('Desculpe, as parcelas estão muito altas para o seu salário!!!')

