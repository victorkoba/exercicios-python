from datetime import datetime
maiorIdade = 0
menorIdade = 0

for i in range(1, 7 + 1):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(i)))
    if (datetime.today().year - ano) >= 18:
        maiorIdade += 1
    else:
        menorIdade += 1

print('Ao todo tivemos {} pessoas maiores de idade\nE também tivemos {} pessoas menores de idade'.format(maiorIdade, menorIdade))