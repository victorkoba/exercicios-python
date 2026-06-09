numerosExtenso = (
    'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
    'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
    'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
    'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    n = int(input('Digite um número: '))
    if n >= 0 and n <= 20:
        break
print(f'{numerosExtenso[n - 1]}')