s = 0
cont = 0
for c in range(1, 500 + 1, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print('A somatória dos {} números ímpares de 1 até 500 que são divisíveis por 3 é de {}'.format(cont,s))