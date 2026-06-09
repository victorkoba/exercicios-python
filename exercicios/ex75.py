num = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
cont = 0
numPar = 0
for i in num:
    if i == 9:
        cont += 1
    if i % 2 == 0:
        numPar += 1
print(cont)
print(num.index(3))
print(numPar)