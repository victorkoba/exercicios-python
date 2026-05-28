num = int(input('Digite um número que deseja fazer a conversão: '))
print('Qual será a base de conversão?\n1 - binário\n2 - octal\n3 - hexadecimal')
opcao = int(input())
if opcao == 1:
    print('O número {} tem seu binário = {}'.format(num, bin(num)))
elif opcao == 2:
    print('O número {} tem seu octadecimal = {}'.format(num, oct(num)))
elif opcao == 3:
    print('O número {} tem seu hexadecimal = {}'.format(num, hex(num)))
else:
    print('Opção inválida!')