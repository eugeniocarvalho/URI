'''
Leia um valor inteiro N. Este valor será a quantidade de
valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do
intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.
'''

num = int(input())
In = 0
Out = 0

for i in range(num):
    r = int(input())

    if 10 <= r <= 20:
        In += 1
    else:
        Out += 1

print('{} in\n{} out'.format(In, Out))
