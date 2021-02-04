def LIS(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return 1

    cache = [0 for i in range(n)]
    cache[0] = 1
    for i in range(1, n):
        maximum = 0
        for j in range(i-1, -1, -1):
            if arr[i] > arr[j] and cache[j] > maximum:
                maximum = cache[j]
        cache[i] = maximum + 1

    print(cache)
    return max(cache)


if __name__ == '__main__':
    # All input works
    # arr = []
    # arr = [5]
    # arr = [2, 3]
    # arr = [3, 2]
    # arr = [3, 10, 2, 1, 20]
    # arr = [50, 3, 10, 7, 40, 80]
    # arr = [10, 22, 9, 33, 21, 50, 41, 60]
    arr = [1, 2, 5, 3, 7, 6, 8, 9]

    print(LIS(arr))
