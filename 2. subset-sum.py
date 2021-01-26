import time
import random
import sys
sys.setrecursionlimit(10**5)
dp = []


def initializeTable(n, s):
    global dp
    dp = []
    dp = [[False for sum in range(s+1)] for item in range(n+1)]


def subsetSum(arr, n, s):
    global dp
    if s == 0:
        return True
    if n == 0:
        return False

    if dp[n-1][s] != 0:
        return dp[n-1][s]

    if arr[n-1] > s:
        dp[n-1][s] = subsetSum(arr, n-1, s)
    elif arr[n-1] <= s:
        dp[n-1][s] = subsetSum(arr, n-1, s-arr[n-1]) or subsetSum(arr, n-1, s)
    return dp[n-1][s]


def subsetSumIter(arr, n, s):
    lookupTable = [[False for sum in range(s+1)] for item in range(n+1)]

    for item in range(s+1):
        lookupTable[0][item] = False

    for sum_ in range(n+1):
        lookupTable[sum_][0] = True

    for item in range(1, n+1):
        for sum_ in range(1, s+1):
            if arr[item-1] > s:
                lookupTable[item][sum_] = lookupTable[item-1][sum_]
            elif arr[item-1] <= s:
                lookupTable[item][sum_] = lookupTable[item - 1][sum_ -
                                                                arr[item-1]] or lookupTable[item-1][sum_]

    return lookupTable[n][s]


if __name__ == '__main__':
    arr = [random.randint(10, 1000) for i in range(20000)]
    s = 52220
    n = len(arr)
    # Recursive
    initializeTable(n, s)
    start = time.time()
    print(subsetSum(arr, n, s))
    print(time.time() - start)
    # Iterative
    start = time.time()
    print(subsetSumIter(arr, n, s))
    print(time.time() - start)
