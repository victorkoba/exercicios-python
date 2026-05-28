from time import sleep
contador = 0
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        print('Finalizando...')
        sleep(0.3)
        break
    else:
        while contador <= 10:
            print(f'{n} X {contador} = {n*contador}')
            contador += 1
        contador = 0
