import random


dp = []


def rodCuttingRecursive(length, value, N, n):
    global dp
    if N <= 0:
        return 0
    if n == 0:
        return 0

    if dp[n-1][N] != 0:
        return dp[n-1][N]

    if length[n-1] > N:
        dp[n-1][N] = rodCuttingRecursive(length, value, N, n-1)
    elif length[n-1] <= N:
        dp[n-1][N] = max(value[n-1] + rodCuttingRecursive(length, value,
                                                          N - length[n-1], n), rodCuttingRecursive(length, value, N, n-1))

    return dp[n-1][N]


def rodCuttingIterative(length, value, N, n):
    cache = [[0 for i in range(N+1)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, N+1):
            if length[i-1] > j:
                cache[i][j] = cache[i-1][j]
            else:
                cache[i][j] = max(value[i-1] + cache[i]
                                  [j - length[i-1]], cache[i-1][j])

    # print(cache)
    return cache[n][N]


if __name__ == '__main__':
    length = [1, 2, 3, 4, 5]
    value = [1, 2, 4, 5, 3]
    N = 5
    n = len(length)

    # Recursive
    dp = [[0 for i in range(N+1)] for j in range(n+1)]
    print(rodCuttingRecursive(length, value, N, n))

    # iterative
    print(rodCuttingIterative(length, value, N, n))
