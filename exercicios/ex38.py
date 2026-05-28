num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
if num1 > num2:
    print('O primeiro valor: {} é maior que o segundo valor: {}!'.format(num1, num2))
elif num1 < num2:
    print('O segundo valor: {} é maior que o primeiro valor: {}!'.format(num2, num1))
else:
    print('O primeiro valor: {} é igual ao segundo valor: {}'.format(num1, num2))