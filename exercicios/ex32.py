ano = int(input('Digite em que ano estamos: '))
if ano % 4 == 0 or ano % 400 == 0:
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto!')