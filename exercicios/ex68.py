from random import randint
contador = 0
while True:
    n = int(input('Digite um valor: '))
    parImpar = input('Par ou Ímpar? [P/I] ').upper()
    computador = randint(0, 10)
    soma = computador + n
    if soma % 2 == 0 and parImpar == 'P':
        print(f'Você jogou {n} e o computador {computador}.'
              f' Total de {soma} e deu PAR!')
        contador += 1
    elif soma % 2 != 0 and parImpar == 'I':
        print(f'Você jogou {n} e o computador {computador}.'
              f' Total de {soma} e deu ÍMPAR!')
        contador += 1
    else:
        print(f'Você jogou {n} e o computador {computador}.'
              f' Total de {soma}! Você perdeu!')
        break
print(f'GAME OVER! Você ganhou {contador} vezes')