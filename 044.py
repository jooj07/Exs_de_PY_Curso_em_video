"""
um programa que calcule o valor a ser pago
à vista dinheiro/cheque: 10% de desconto
à vista cartão: 5% de desconto
até 2x no coartão: preço normal
3x ou mais no cartão: 20% de juros
"""
preconormal = float(input('Digite o valor do produto: R$'))
forma = int(input("""
Escolha a forma de pagamento: 
1 - À vista dinheiro/cheque: 10% de desconto
2 - À vista cartão: 5% de desconto
3 - Até 2x no coartão: preço normal 
4 - 3x ou mais no cartão: 20% de juros 
Forma de pagamento: """))
if forma == 1:
    desc10 = preconormal - (preconormal*0.10)
    print(f'Total a pagar: R${desc10}')
elif forma == 2:
    desc5 = preconormal - (preconormal * 0.05)
    print(f'Total a pagar: R${desc5}')
elif forma == 3:
    print(f'Total a pagar: R${preconormal}')
elif forma == 4:
    juros20 = preconormal + (preconormal * 0.20)
    print(f'Total a pagar: R${juros20}')
