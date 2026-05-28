contador = 0
mais1000 = 0
barato = ''
menorPreco = 0
total = 0
while True:
    produto = input('Digite o nome do produto: ').strip().upper()
    preco = float(input('Digite o preço do produto: '))
    contador += 1
    total += preco
    if preco > 1000:
        mais1000 += 1
    if contador == 1 or preco < menorPreco:
        menorPreco = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break

print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi a {barato} que custa {menorPreco}')