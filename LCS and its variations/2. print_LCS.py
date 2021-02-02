cache = []


def LCSLength(x, y, n, m):
    global cache
    if n == 0 or m == 0:
        return 0

    if cache[n-1][m-1] != 0:
        return cache[n-1][m-1]
    elif x[n - 1] == y[m - 1]:
        cache[n-1][m-1] = 1 + LCSLength(x, y, n - 1, m - 1)
    else:
        cache[n-1][m-1] = max(LCSLength(x, y, n - 1, m),
                              LCSLength(x, y, n, m-1))

    return cache[n-1][m-1]


def LCSLengthIter(x, y, n, m):
    cache = [[0 for i in range(m+1)] for i in range(n+1)]
    lcs_string = ''
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

    # return cache[n-1][m-1]

    len_x = n
    len_y = m
    lcs_string = ""
    while len_x > 0 and len_y > 0:
        if x[len_x-1] == y[len_y-1]:
            lcs_string += x[len_x-1]
            len_x -= 1
            len_y -= 1
        else:
            if cache[len_x-1][len_y] > cache[len_x][len_y-1]:
                len_x -= 1
            else:
                len_y -= 1
    return lcs_string[::-1]


if __name__ == '__main__':
    x = 'ahbjnk'
    y = 'abjnck'
    n = len(x)
    m = len(y)

    # Recursive
    cache = [[0 for i in range(m+1)] for j in range(n+1)]
    print(LCSLength(x, y, n, m))

    # Iterative
    print(LCSLengthIter(x, y, n, m))
