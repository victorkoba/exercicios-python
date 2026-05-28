km = float(input('Quantos km você rodou com o carro? '))
dias = int(input('Por quantos dias ele foi alugado? '))
preco = (km * 0.15) + (dias * 60)
print('O preço a pagar pelo aluguel foi de R${:.2f}'.format(preco))