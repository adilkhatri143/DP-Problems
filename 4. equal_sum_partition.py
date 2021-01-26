import random
import time


def subsetSum(arr, n, sum_of_array):
    lookupTable = [[False for i in range(sum_of_array+1)] for j in range(n+1)]

    for i in range(sum_of_array+1):
        lookupTable[0][i] = False

    for j in range(n+1):
        lookupTable[j][0] = True

    for item in range(1, n+1):
        for sum_ in range(1, sum_of_array+1):
            if arr[item-1] > sum_:
                lookupTable[item][sum_] = lookupTable[item-1][sum_]
            elif arr[item-1] <= sum_:
                lookupTable[item][sum_] = lookupTable[item -
                                                      1][sum_ - arr[item - 1]] or lookupTable[item-1][sum_]

    return lookupTable[n][sum_of_array]


if __name__ == '__main__':
    # arr = [random.randint(10, 10000) for i in range(100)]
    arr = [3, 3, 2]
    sum_of_array = sum(arr)
    n = len(arr)
    if sum_of_array % 2 == 0:
        start = time.time()
        print(subsetSum(arr, n, sum_of_array//2))
        print(time.time() - start)
    else:
        print('Partiton not possible because array sum is odd.')
