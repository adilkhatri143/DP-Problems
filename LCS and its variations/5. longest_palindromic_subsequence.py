
def LPS(x, y, n, m):
    cache = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                cache[i][j] = 1 + cache[i-1][j-1]
            else:
                cache[i][j] = max(cache[i-1][j], cache[i][j-1])

    i = len(x)
    j = len(y)
    s = ''

    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            s += x[i-1]
            i -= 1
            j -= 1
        else:
            if x[i-1] > y[j-1]:
                i -= 1
            else:
                j -= 1

    return s


if __name__ == '__main__':
    x = 'axbcbcbza'
    y = x[::-1]
    n = len(x)
    m = len(y)

    print(LPS(x, y, n, m))
