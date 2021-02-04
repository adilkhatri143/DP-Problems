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

    return cache[n][m]


if __name__ == '__main__':
    x = 'aexbcbda'
    y = x[::-1]
    n = len(x)
    m = len(y)

    # Iterative
    print(n - LCSLengthIter(x, y, n, m))
