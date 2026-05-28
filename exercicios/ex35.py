r1 = float(input('Primeiro valor: '))
r2 = float(input('Segundo valor: '))
r3 = float(input('Terceiro valor: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Você pode formar um triângulo!')
else:
    print('Você não pode formar um triângulo!')