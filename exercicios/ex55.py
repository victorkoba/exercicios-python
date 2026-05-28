listaPeso = []
for c in range(1, 5 + 1):
    peso = float(input('Digite o peso da {}° pessoa: '.format(c)))
    listaPeso.append(peso)
print('O maior peso lido foi de {}Kg'.format(max(listaPeso)))
print('O menor peso lido foi de {}Kg'.format(min(listaPeso)))