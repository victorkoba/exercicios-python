salario = float(input('Qual o seu salario: '))
if salario > 1250:
    salario = salario + (salario * 0.10)
    print('Seu salário foi para {} reais'.format(salario))
else:
    salario = salario + (salario * 0.15)
    print('Seu salário foi para {} reais'.format(salario))