sexo = input("Digite o sexo [M/F]: ").upper()
while sexo not in "MF":
    print("Digite novamente, sexo inválido!")
    sexo = input("Digite o sexo [M/F]: ").upper()
if sexo == "M":
    print('Você é homem!')
else:
    print('Você é mulher!')