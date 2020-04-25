'''
Leia 6 valores. Em seguida, mostre quantos destes valores digitados
foram positivos. Na próxima linha, deve-se mostrar a média de todos
os valores positivos digitados, com um dígito após o ponto decimal.
'''

cont = 0
media = 0

for i in range(6):
    num = float(input())

    if num > 0:
        cont += 1
        media += num

media = media / cont

print('{} valores positivos\n{:.1f}'.format(cont, media))
