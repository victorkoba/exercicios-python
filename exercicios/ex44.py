print('{:=^40}'.format(' Lojas Koba '))
valor = float(input('Valor a ser pago pelo produto: '))
print('Qual a forma de pagamento?\n1. À vista dinheiro/cheque\n2. À vista no cartão\n3. Em até 2x no cartão\n4. 3x ou mais no cartão')
opcao = int(input('Qual opção de pagamento: '))
if opcao == 1:
    desconto = valor * 0.10
    print('O valor da compra é R${}, porém teve um desconto de R${} e o valor ficou R${}'.format(valor, desconto, valor - desconto))
elif opcao == 2:
    desconto = valor * 0.05
    print('O valor da compra é R${}, porém teve um desconto de R${} e o valor ficou R${}'.format(valor, desconto, valor - desconto))
elif opcao == 3:
    print('O valor da compra é R${}, não possui nenhum desconto'.format(valor))
elif opcao == 4:
    juros = valor * 0.20
    print('O valor da compra é R${}, porém teve juros de R${} e o valor ficou R${}'.format(valor, juros, valor + juros))
else:
    print('Ipção inválida!')