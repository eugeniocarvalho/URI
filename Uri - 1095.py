'''
I=1 J=60
I=4 J=55
I=7 J=50
...
I=? J=0
'''

i = 1
j = 60

while j >= 0:
    print('I={} J={}'.format(i, j))
    j -= 5
    i += 3
