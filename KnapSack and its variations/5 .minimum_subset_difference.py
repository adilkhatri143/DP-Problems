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

    return lookupTable[n]


if __name__ == '__main__':
    arr = [1, 6, 12, 5]
    sum_of_array = sum(arr)
    n = len(arr)

    last_row = subsetSumIter(arr, n, sum_of_array)

    new_arr = []
    for item in range(len(last_row) // 2 + 1):
        if last_row[item] == True:
            new_arr.append(item)

    print(new_arr)
    minimum = float('inf')

    for i in range(len(new_arr)):
        minimum = min(sum_of_array - 2 * new_arr[i], minimum)

    print(minimum)
