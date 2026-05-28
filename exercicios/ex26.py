frase = input('Digite uma frase: ').upper().strip()
a = frase.count('A')
primeiraVez = frase.find('A')
ultimaVez = frase.rfind('A')
print('A frase têm {} letras A, aparece a primeira vez na posição {} e a última vez na posição {}'
      ''.format(a,primeiraVez,ultimaVez))