'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.'''

reais = float(input('Quantos reais você ganha por hora trabalhada? R$ '))
horas = int(input('Quantas horas foram trabalhadas no mês? '))
salario = reais * horas
print('O salário referente a esse mês foi de R${:.2f}.'.format(salario))
