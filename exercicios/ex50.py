soma = 0
for c in range(1, 6 +1):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
print('A soma de todos os números pares digitados é de {}'.format(soma))