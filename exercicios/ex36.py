valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = valor / (anos * 12)
minimo = salario * 0.30
if prestacao < minimo:
    print('Empréstimo aprovado! O valor da parcela R${} não excede 30% do seu salario R${}, portanto 30% é R%{}'.format(prestacao, salario, minimo))
else:
    print('Empréstimo reprovado! O valor da parcela R${} excede 30% do seu salario R${}, portanto 30% é R%{}'.format(prestacao, salario, minimo))