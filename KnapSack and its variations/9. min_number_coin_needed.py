dp = []


def minNoOfCoin(arr, N, n):
    global dp
    if N == 0:
        return 0
    if n == 0:
        return float('inf')

    if dp[n-1][N] != 0:
        return dp[n-1][N]

    if arr[n-1] > N:
        dp[n-1][N] = minNoOfCoin(arr, N, n-1)
    elif arr[n-1] <= N:
        dp[n-1][N] = min(1 + minNoOfCoin(arr, N - arr[n-1], n),
                         minNoOfCoin(arr, N, n-1))

    return dp[n-1][N]


def minNoOfCoinIter(arr, N, n):
    cache = [[0 for i in range(N+1)] for j in range(n+1)]

    for i in range(N+1):
        cache[0][i] = float('inf')

    for j in range(1, n+1):
        cache[j][0] = 0

    for i in range(1, n+1):
        for j in range(1, N+1):
            if arr[i-1] > j:
                cache[i][j] = cache[i-1][j]
            else:
                cache[i][j] = min(1 + cache[i][j - arr[i-1]], cache[i-1][j])

    return cache[n][N]


if __name__ == '__main__':
    arr = [1, 1, 2]
    N = 5
    n = len(arr)
    dp = [[0 for i in range(N+1)] for j in range(n+1)]
    # Recursive
    print(minNoOfCoin(arr, N, n))

    # Iterative
    print(minNoOfCoinIter(arr, N, n))
