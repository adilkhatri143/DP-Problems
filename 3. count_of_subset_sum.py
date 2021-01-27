import random


def countSubset(arr, n, s):
    lookupTable = [[0 for i in range(s+1)] for j in range(n+1)]

    for i in range(s+1):
        lookupTable[0][i] = 0

    for i in range(n+1):
        lookupTable[i][0] = 1

    for item in range(1, n+1):
        for sum_ in range(1, s+1):
            if arr[item-1] > sum_:
                lookupTable[item][sum_] = lookupTable[item-1][sum_]
            elif arr[item-1] <= sum_:
                lookupTable[item][sum_] = lookupTable[item -
                                                      1][sum_ - arr[item-1]] + lookupTable[item-1][sum_]

    return lookupTable[n][s]


if __name__ == '__main__':
    arr = [random.randint(10, 1000) for i in range(10000)]
    s = 5222
    n = len(arr)
    print(countSubset(arr, n, s))
