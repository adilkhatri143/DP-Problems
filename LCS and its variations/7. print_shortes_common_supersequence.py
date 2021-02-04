def LCSLengthIter(x, y, n, m):
    cache = [[0 for i in range(m+1)] for i in range(n+1)]

    for i in range(m+1):
        cache[0][i] = 0

    for j in range(n+1):
        cache[j][0] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                cache[i][j] = 1 + cache[i - 1][j - 1]
            else:
                cache[i][j] = max(cache[i-1][j], cache[i][j-1])

    # return cache[n][m]

    i = n
    j = m
    scs = ''

    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            scs += x[i-1]
            i -= 1
            j -= 1
        else:
            if cache[i][j-1] > cache[i-1][j]:
                scs += y[j-1]
                j -= 1
            else:
                scs += x[i-1]
                i -= 1

    while i > 0:
        scs += x[i-1]
        i -= 1

    while j > 0:
        scs += y[j-1]
        j -= 1

    return scs[::-1]


if __name__ == '__main__':
    # x = 'AGGTAB'
    # y = 'GXTXAYB'
    x = 'ACBCF'
    y = 'ABCDAF'
    n = len(x)
    m = len(y)

    # Iterative
    print(LCSLengthIter(x, y, n, m))
