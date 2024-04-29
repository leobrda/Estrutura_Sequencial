'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a) salário bruto.
b) quanto pagou ao INSS.
c) quanto pagou ao sindicato.
d) o salário líquido.
Calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$'''

ganho = float(input('Quantos reais você ganha por hora trabalhada? R$ '))
horas = int(input('Quantas horas trabalhadas no mês? '))
total_salario = ganho * horas
ir = total_salario * 11 / 100
inss = total_salario * 8 / 100
sindicato = total_salario * 5 / 100
liquido = total_salario - ir - inss - sindicato
print('+ Salário bruto: R${:.2f}'.format(total_salario))
print('- IR (11%): R${:.2f}'.format(ir))
print('- INSS (8%): R${:.2f}'.format(inss))
print('- Sindicado (5%): R${:.2f}'.format(sindicato))
print('= Salário Líquido: R${:.2f}'.format(liquido))
