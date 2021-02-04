def LPS(x, y, n, m):
    cache = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                cache[i][j] = 1 + cache[i-1][j-1]
            else:
                cache[i][j] = max(cache[i-1][j], cache[i][j-1])

    return cache[n][m]


if __name__ == '__main__':
    x = 'axbcbbza'
    y = x[::-1]
    n = len(x)
    m = len(y)

    print(n - LPS(x, y, n, m))
