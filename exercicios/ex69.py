maioresIdade = 0
homens = 0
mulheres20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo (M/F): ').upper()
    while sexo not in 'MF':
        sexo = input('Digite seu sexo (M/F): ').upper()
    if idade > 18:
        maioresIdade += 1
    elif sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres20 += 1
    continuar = input('Você quer continuar? ').upper()
    if continuar not in 'SN':
        continuar = input('Você quer continuar? ').upper()
    elif continuar == 'N':
        break
print(f'Têm {maioresIdade} pessoa(s) com mais de 18 anos, {homens} são/é homem(ns) '
      f'e têm {mulheres20} mulher(es) com menos de 20 anos')