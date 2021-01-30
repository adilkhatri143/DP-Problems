import sys
sys.setrecursionlimit(10**6)
dp = []


def coinChangeRecursive(arr, C, n):
    global dp
    if C == 0:
        return 1
    elif C < 0:
        return 0
    elif n <= 0:
        return 0

    if dp[n-1][C] != 0:
        return dp[n-1][C]

    if arr[n-1] > C:
        dp[n-1][C] = coinChangeRecursive(arr, C, n-1)
    elif arr[n-1] <= C:
        dp[n-1][C] = coinChangeRecursive(arr, C - arr[n-1], n) + \
            coinChangeRecursive(arr, C, n-1)
    return dp[n-1][C]


def coinChangeIterative(arr, C, n):
    cache = [[0 for i in range(C+1)] for j in range(n+1)]

    for i in range(C+1):
        cache[0][i] = 0

    for j in range(n+1):
        cache[j][0] = 1

    for i in range(1, n+1):
        for j in range(1, C+1):
            if arr[i-1] > j:
                cache[i][j] = cache[i-1][j]
            else:
                cache[i][j] = cache[i][j - arr[i-1]] + cache[i-1][j]

    return cache[n][C]


if __name__ == "__main__":
    arr = [1, 2, 5, 1, 1, 5]
    C = 6
    n = len(arr)

    # Recursive
    dp = [[0 for i in range(C+1)] for j in range(n+1)]
    print(coinChangeRecursive(arr, C, n))

    # iteratve
    print(coinChangeIterative(arr, C, n))
