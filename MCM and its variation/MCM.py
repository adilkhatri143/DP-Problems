cache = []


def solveMCM(arr, i, j):
    global cache
    if i >= j:
        return 0

    if(cache[i][j] != -1):
        return cache[i][j]

    minimum = float('inf')
    for k in range(i, j):
        temp = solveMCM(arr, i, k) + solveMCM(arr, k+1, j) + \
            (arr[i-1] * arr[k] * arr[j])

        if temp < minimum:
            minimum = temp

    cache[i][j] = minimum
    return minimum


if __name__ == "__main__":
    arr = [40, 10, 30, 20, 4, 56, 43, 23, 45, 32, 43, 23, 45, 46, 78, 99]

    i = 1
    j = len(arr)-1
    cache = [[-1 for i in range(len(arr)+1)] for j in range(len(arr)+1)]
    print(solveMCM(arr, i, j))
