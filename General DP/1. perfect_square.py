'''
sum = 12
1 + 1 + 1 + ... + 1 = 12 = 12 times (1^2)

(2^2) + (2^2) + (2^2) = 12 = 3 times

(3^2) + 1 + 1 + 1 + 1 = 12 = 4 times

like many combination. find least!
'''


if __name__ == '__main__':
    s = 12

    cache = [float('inf') for i in range(s+1)]
    cache[0] = 0

    i = 1
    while i <= s:
        j = 1
        while j * j <= i:
            cache[i] = min(cache[i], 1 + cache[i - j * j])
            j += 1
        i += 1

    print(cache[s])
