while 1:
    sum = 0
    result = ''

    res = input().strip()

    res = res.split()

    n1 = int(res[0])
    n2 = int(res[1])

    if n1 <= 0 or n2 <= 0:
        break
    if n1 <= n2:
        for n1 in range(n1, n2+1):
            if n1 > 0:
              sum += n1
              result += str(n1) + ' '
    else:
        for n2 in range(n2, n1+1):
            if n2 > 0:
                sum += n2
                result += str(n2) + ' '

    result += 'Sum=%d'
    print(result %sum)