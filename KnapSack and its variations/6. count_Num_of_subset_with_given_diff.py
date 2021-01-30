import time
import random
import sys
sys.setrecursionlimit(10**6)

dp = []


def initdp(n, s):
    global dp
    dp = [[0 for i in range(s+1)] for j in range(n+1)]


def subsetSum(arr, n, s):
    global dp
    if s == 0:
        return 1
    if n == 0:
        return 0

    if dp[n-1][s] != 0:
        return dp[n-1][s]

    if arr[n-1] > s:
        dp[n-1][s] = subsetSum(arr, n-1, s)
    elif arr[n-1] <= s:
        dp[n-1][s] = subsetSum(arr, n-1, s - arr[n-1]) + subsetSum(arr, n-1, s)
    return dp[n-1][s]


def subsetSumIter(arr, n, s):
    lookupTable = [[0 for i in range(s+1)] for j in range(n+1)]

    for item in range(s+1):
        lookupTable[0][item] = 0

    for sum_ in range(n+1):
        lookupTable[sum_][0] = 1

    for item in range(1, n+1):
        for sum_ in range(1, s+1):
            if arr[item-1] > sum_:
                lookupTable[item][sum_] = lookupTable[item-1][sum_]
            elif arr[item-1] <= sum_:
                lookupTable[item][sum_] = lookupTable[item -
                                                      1][sum_ - arr[item-1]] + lookupTable[item-1][sum_]

    return lookupTable[n][s]


if __name__ == '__main__':
    # arr = [1, 1, 2, 3]
    arr = [random.randint(10, 1000) for i in range(30)]
    diff = 660
    sum_of_array = sum(arr)
    n = len(arr)

    s = (diff + sum_of_array) // 2
    # Recursive
    initdp(n, s)
    start = time.time()
    print(subsetSum(arr, n, s))
    print(time.time() - start)
    # Iterative
    start = time.time()
    print(subsetSumIter(arr, n, s))
    print(time.time() - start)
