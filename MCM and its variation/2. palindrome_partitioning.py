cache = []


def isPalindrome(s):
    return s == s[::-1]


def palindrome_part(s, i, j):
    global cache
    if i >= j or isPalindrome(s[i: j+1]):
        return 0

    if cache[i][j] != -1:
        return cache[i][j]

    minimum = float('inf')
    for k in range(i, j):
        temp = 1 + palindrome_part(s, i, k) + palindrome_part(s, k + 1, j)
        minimum = min(temp, minimum)

    cache[i][j] = minimum
    return minimum


if __name__ == "__main__":
    # s = 'abaaabcbbcxabcd'
    s = 'madam'
    i = 0
    j = len(s) - 1

    cache = [[-1 for i in range(len(s)+1)] for j in range(len(s)+1)]
    print(palindrome_part(s, i, j))
