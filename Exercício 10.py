'''Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Fahrenheit.'''

c = float(input('Informe a temperatura em ºC: '))
f = (c * 9 / 5) + 32
print('{}ºC são {:.2f}ºF.'.format(c, f))