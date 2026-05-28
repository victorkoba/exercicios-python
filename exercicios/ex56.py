somaidade = 0
mediaidade = 0
maioridadeHomem = 0
nomeVelho = ''
totmulher20 = 0
for c in range(1,4 + 1):
    print('----- {}° Pessoa -----'.format(c))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maioridadeHomem:
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média da idade do grupo é de {} anos'. format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadeHomem, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))