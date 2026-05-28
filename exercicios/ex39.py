from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano_nascimento

if idade < 18:
    tempo = 18 - idade
    print('Você tem {} anos, então faltam {} anos para você se alistar.'.format(idade, tempo))
elif idade > 18:
    tempo = idade - 18
    print('Você tem {} anos, então já passou da hora de se alistar, você está {} anos atrasado.'.format(idade, tempo))
else:
    print('Seu alistamento é nesse ano!')