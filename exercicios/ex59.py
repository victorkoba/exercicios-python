from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
while True:
    print('----- MENU -----')
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')
    n = int(input('Digite o número desejado: '))
    if n == 1:
        soma = n1 + n2
        print('A soma dos dois números é {}'.format(soma))
        sleep(0.5)
    elif n == 2:
        multiplicar = n1 * n2
        print('A multiplicação dos dois números é {}'.format(multiplicar))
        sleep(0.5)
    elif n == 3:
        maior = n1
        if maior > n2:
            print(maior)
        elif maior < n2:
            maior = n2
            print(maior)
        else:
            print('Os dois são iguais!')
        sleep(0.5)
    elif n == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        sleep(0.5)
    elif n == 5:
        print('Finalizando...')
        sleep(0.5)
        break
    else:
        print('Digite um valor correto!')
        sleep(0.5)