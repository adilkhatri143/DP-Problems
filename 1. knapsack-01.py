dp = [[0 for x in range(6)] for x in range(4)]


def knapsack(val, wet, w, n):
    global dp
    if w == 0 or n == 0:
        return 0

    if dp[n-1][w] != 0:
        return dp[n-1][w]

    if wet[n-1] > w:
        dp[n-1][w] = knapsack(val, wet, w, n-1)
    elif wet[n-1] <= w:
        dp[n-1][w] = max(val[n-1] + knapsack(val, wet, w -
                                             wet[n-1], n-1), knapsack(val, wet, w, n-1))
    return dp[n-1][w]


if __name__ == '__main__':
    val = [60, 100, 120]
    wet = [1, 2, 3]
    w = 5
    n = len(val)

    # Iterative
    lookupTable = [[0 for x in range(w + 1)] for x in range(n + 1)]
    for row in range(n+1):
        for col in range(w+1):
            if row == 0 or col == 0:
                lookupTable[row][col] = 0
            elif wet[row-1] <= col:
                lookupTable[row][col] = max(val[row-1] + lookupTable[row-1]
                                            [col-wet[row-1]], lookupTable[row-1][col])
            elif wet[row-1] > col:
                lookupTable[row][col] = lookupTable[row-1][col]
    print(lookupTable[n][w])

    # Recursive
    print(knapsack(val, wet, w, n))
