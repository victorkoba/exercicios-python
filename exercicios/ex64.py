n = int(input('Digite um número: '))
contador = 0
soma = 0
while n != 999:
    contador += 1
    soma += n
    n = int(input('Digite um número: '))

print(f'A quantidade de números digitados foi {contador}')
print(f'A soma de todos os números digitados foi {soma}')