'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de
1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
a) comprar apenas latas de 18 litros;
b) comprar apenas galões de 3,6 litros;
c) misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

tamanho = float(input('Quantos metros quadrados da área a ser pintada? '))
litro = tamanho / 6
lata = litro / 18 #R$80
galao = litro / 3.6 #R$25
total_lata = lata * 80
total_galao = galao * 25
litros_necessarios = tamanho / 6 * 1.1
latas = int(litros_necessarios // 18)
litros_restantes = litros_necessarios % 18
galoes = litros_restantes / 3.6
total_mistura = (latas * 80) + (galoes * 25)

print('Você vai precisar comprar {:.2f} litros de tinta.'.format(litro))
print('Comprando apenas latas de 18 litros você vai pagar R${:.2f}.'.format(total_lata))
print('Comprando apenas galões de 3.6 litros você vai pagar R${:.2f}.'.format(total_galao))
print('Misturando latas e galões você vai pagar R${:.2f}.'.format(total_mistura))

