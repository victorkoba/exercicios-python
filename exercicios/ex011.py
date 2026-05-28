largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
tinta = area / 2
print('A parede possui {} metros de largura e {} metros de altura,\nsua área é de {} metros quadrados '
      'e você precisará de {} litros de tinta'.format(largura, altura, area, tinta))