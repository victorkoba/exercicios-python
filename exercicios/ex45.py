from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('\n [0] Pedra\n [1] Papel\n [2] Tesoura')
pessoa = int(input('Escolha uma das opções: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if computador == 0:
    if pessoa == 0:
        print('O computador escolheu {} e você escolheu {}\n Empate!'.format(itens[computador], itens[pessoa]))
    elif pessoa == 1:
        print('O computador escolheu {} e você escolheu {}\n Você ganhou!'.format(itens[computador], itens[pessoa]))
    elif pessoa == 2:
        print('O computador escolheu {} e você escolheu {}\n Computador ganhou!'.format(itens[computador], itens[pessoa]))
    else:
        print('Jogada Inválida!')

if computador == 1:
    if pessoa == 0:
        print('O computador escolheu {} e você escolheu {}\n Computador ganhou!'.format(itens[computador], itens[pessoa]))
    elif pessoa == 1:
        print('O computador escolheu {} e você escolheu {}\n Empate!'.format(itens[computador], itens[pessoa]))
    elif pessoa == 2:
        print('O computador escolheu {} e você escolheu {}\n Você ganhou!'.format(itens[computador], itens[pessoa]))
    else:
        print('Jogada Inválida!')

if computador == 2:
    if pessoa == 0:
        print('O computador escolheu {} e você escolheu {}\n Você ganhou!'.format(itens[computador], itens[pessoa]))
    elif pessoa == 1:
        print('O computador escolheu {} e você escolheu {}\n Computador ganhou!'.format(itens[computador], itens[pessoa]))
    elif pessoa == 2:
        print('O computador escolheu {} e você escolheu {}\n Empate!'.format(itens[computador], itens[pessoa]))
    else:
        print('Jogada Inválida!')