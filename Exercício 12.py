'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58'''

altura = float(input('Informe a sua altura em metros: '))
peso_ideal = (72.7 * altura) - 58
print('O seu peso ideal é {:.2f}Kg.'.format(peso_ideal))
