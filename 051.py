#10 primeiros termos de uma progressão aritmética
prim_termo = int(input('Qual o primeiro termo? '))
razao = int(input('E qual a razão? '))
decimotermo = prim_termo + (10 - 1) * razao
for c in range(prim_termo, decimotermo + razao, razao):
    print(f'{c}', end=' → ')
print('ACABOU!')
