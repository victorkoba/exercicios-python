v = float(input('Digite a velocidade do carro: '))
if v > 80:
    print('Você foi multado')
    valor = (v - 80)*7
    print('O valor da multa foi de {} reais'.format(valor))
else:
    print('Você está dentro do limite!')