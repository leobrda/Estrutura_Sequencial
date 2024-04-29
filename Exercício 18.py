'''Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado
de download do arquivo usando este link (em minutos).'''

arquivo = float(input('O arquivo tem quantos MB? '))
internet = int(input('A velocidade da internet é de quantos Mbps? '))
tempo = arquivo / (internet / 8) #tempo em segundos
tempo_min = tempo / 60

print('O seu download vai demorar {:.2f} minutos para terminar.'.format(tempo_min))
