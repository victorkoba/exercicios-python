primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro
c = 1
while c <= 10:
    print(f'{termo}', end='')
    print(' -> ' if c < 10 else '', end='')
    termo += razao
    c += 1
print('\nFIM')