termos = int(input('Quantos termos você quer exibir? '))
a = 0
b = 1
c = 0
while c < termos:
    print(f'{a} -> ', end='')
    proximo = a + b
    a = b
    b = proximo
    c += 1
print('FIM')