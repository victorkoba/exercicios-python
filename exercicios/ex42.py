r1 = float(input('Primeiro valor: '))
r2 = float(input('Segundo valor: '))
r3 = float(input('Terceiro valor: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Os segmentos podem formar um triângulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os segmentos não podem formar um triângulo!')