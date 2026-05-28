from random import randint
nEscolhido = randint(0,5)
nDigitado = int(input('Digite um número: '))

if nDigitado == nEscolhido:
    print('Você venceu!')
else:
    print('Você perdeu!')