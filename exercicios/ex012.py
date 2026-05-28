preco = float(input('Digite o preço do produto: '))
desconto = preco - (preco * 5 /100)
print('O preço original é R${}, mas'
      ' depois do desconto ficou R${}'.format(preco,desconto))