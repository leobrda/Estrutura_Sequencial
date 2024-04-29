'''Faça um Programa que calcule a área de um quadrado,
em seguida mostre o dobro desta área para o usuário.'''

lado = float(input('Informe o lado do quadrado: '))
area_quad = lado * lado
dobro = area_quad * 2
print('A área do quadrado é {}.'.format(area_quad))
print('O dobro dessa área é {}.'.format(dobro))
