'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

altura = float(input('Informe a sua altura em metros: '))
peso_homem = (72.7 * altura) - 58
peso_mulher = (62.1 * altura) - 44.7

print('O peso ideal para homem é {:.2f}Kg.'.format(peso_homem))
print('O peso ideal para mulher é {:.2f}Kg.'.format(peso_mulher))
