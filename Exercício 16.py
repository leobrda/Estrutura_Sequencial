'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de
1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

tamanho = float(input('Quantos metros quadrados da área a ser pintada? '))

litro = tamanho / 3
lata = litro / 18
total = lata * 80

print('Você vai precisar de {:.2f} litros de tinta para pintar essa área.'.format(litro))
print('Você vai precisar de {:.2f} latas de tinta.'.format(lata))
print('O total a pagar é de R${:.2f}.'.format(total))