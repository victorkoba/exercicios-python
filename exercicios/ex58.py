from random import randint
tentativas = 1
nEscolhido = randint(0,10)
nDigitado = int(input('Digite um número: '))
while nDigitado != nEscolhido:
    tentativas += 1
    print('Tente novamente!')
    nDigitado = int(input('Digite um número: '))
print(f'Foi necessário {tentativas} tentativas para acertar!')
print(f'O número escolhido foi {nEscolhido}')