'''Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
1) O produto do dobro do primeiro com metade do segundo .
2) A soma do triplo do primeiro com o terceiro.
3) O terceiro elevado ao cubo.'''

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
#1
produto = (n1 * 2) * (n2 /2)
#2
soma = (n1 * 3) + n3
#3
terceiro = n3 ** 3
print('1) O produto do dobro do primeiro com metado do segundo é {}.'.format(produto))
print('2) A soma do triplo do primeiro com o terceiro é {}.'.format(soma))
print('3) O terceiro elevado ao cubo é {}.'.format(terceiro))

