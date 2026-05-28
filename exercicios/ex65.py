n = int(input('Digite um número: '))
soma = 0
contador = 0
maiorNumero = n
menorNumero = n
while True:
    soma += n
    contador += 1
    media = soma / contador
    if maiorNumero < n:
        maiorNumero = n
    if menorNumero > n:
        menorNumero = n
    continuar = input('Você quer continuar? (S/N)').upper()
    if continuar == 'N':
        break
    else:
        n = int(input('Digite um número: '))
print(soma)
print(contador)
print(f"{media:.2f}")
print(maiorNumero)
print(menorNumero)