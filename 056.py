'''
Leia nome, idade e sexo de 4 pessoas
diga:
- a media de idade do grupo
- qual é o nome do homem mais velho
- quantas mulheres têm menos de 20 anos
'''

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher_20 = 0
# -------------------------------------------------------
for p in range(1, 5):
    print(f'--- {p}ª pessoa ---')
    nome = str(input('Nome:')).strip().title()
    idade = int(input('Digite a idade: '))
    sex = str(input('Digite o sexo [M/F]: ')).strip()
    pessoa = {
        'nome': nome,
        'idade': idade,
        'sexo': sex}
    soma_idade += pessoa['idade']
    if p == 1 and pessoa['sexo'] in 'Mm':
        maior_idade_homem = pessoa['idade']
        nome_velho = pessoa['nome']
    if pessoa['sexo'] in 'Mm' and pessoa['idade'] > maior_idade_homem:
        maior_idade_homem = pessoa['idade']
        nome_velho = pessoa['nome']
    if pessoa['sexo'] in 'Ff' and idade < 20:
        tot_mulher_20 += 1
media_idade = soma_idade / 4
print(f'A mida de idades do grupo e de {media_idade} anos')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}')
print(f'Ao todo existem {tot_mulher_20} mulheres com menos de vinte anos')
