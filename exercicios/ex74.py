from random import randint

sorteado = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

for n in sorteado:
    print(n, end=' ')

print(f'\nO maior número foi: {max(sorteado)}')
print(f'\nO maior número foi: {min(sorteado)}')