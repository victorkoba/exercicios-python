nome = input('Digite seu nome completo: ').split()
print('Muito prazer em te conhecer {}!'.format(' '.join(nome)))
print('Seu primeiro nome é {} e o seu último nome é {}'.format(nome[0], nome[len(nome)-1]))