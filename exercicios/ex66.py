soma = 0
contador = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    else:
        contador += 1
        soma += n
print(f'A soma dos {contador} número(s) foi de {soma}')