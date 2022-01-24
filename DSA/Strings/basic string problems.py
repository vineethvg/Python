from collections import Counter
# =============================================================================

# Maximum length of consecutive 1’s in a binary string in
# Python using Map function

# def sol(str):
#     return max(map(len, str.split('0')))


# if __name__ == "__main__":
#     str = '11000111101010111'
#     print(sol(str))
# =============================================================================

# Python code to print common characters
# of two Strings in alphabetical order


# def sol(str1, str2):
#     dict1 = Counter(str1)
#     dict2 = Counter(str2)
#     cD = dict1 & dict2

#     if len(cD) == 0:
#         print -1
#         return

#     commonChars = list(cD.elements())
#     commonChars.sort()
#     return(''.join(commonChars))


# if __name__ == "__main__":
#     str1 = 'bcbb'
#     str2 = 'cbcbd'
#     print(sol(str1, str2))

# =============================================================================

# Smallest number with sum of digits as N and
# divisible by 10^N

# def sol(n):
#     if (n == 0):
#         print("0", end="")

#     if (n % 9 != 0):
#         print(n % 9, end="")
#     for i in range(1, int(n/9) + 1):
#         print("9", end="")

#     for i in range(1, n+1):
#         print("0", end="")
#     print()


# n = 5
# sol(n)
# =============================================================================

# Longest subsequence where every character appears at-least k times

def sol(str):
    for i in str:
        for j in str:
