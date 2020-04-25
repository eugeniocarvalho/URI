'''
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares,
quantos valores digitados foram ímpares, quantos valores digitados foram positivos
e quantos valores digitados foram negativos.
'''

par = 0
impar = 0
pos = 0
neg = 0

for i in range(5):
    num = int(input())

    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
        num *= -1

    if num % 2 == 0:
        par += 1
    else:
        impar += 1

print('{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)'.format(par,
                                                                                                                impar,
                                                                                                                pos,
                                                                                                                neg))
