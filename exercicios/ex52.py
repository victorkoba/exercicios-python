n = int(input('Digite um número: '))
divisivel = 0

for c in range(1, n + 1):
    if n % c == 0:
        divisivel += 1
        print(f'\033[32m{c}\033[m', end=' ')
    else:
        print(f'\033[31m{c}\033[m', end=' ')

if divisivel == 2:
    print(f'\nO número {n} foi divisível {divisivel} vezes\nE por isso ele é primo!')
else:
    print(f'\nO número {n} foi divisível {divisivel} vezes\nE por isso ele não é primo!')