# PROBLEM STATEMENT
# Length of the longest substring with every character
# appearing even number of times

# Input: S = “324425”
# Output: 4

# Explanation: Two substrings consisting of even frequent elements only are “44”
# and “2442”. Since “2442” is the longer of the two, print 4 as the required
# answer.

# Input: S = “223015150”
#Output: 6

# Explanation: Three substrings consisting of even frequent elements only are
# “22”, “1515” and “015150”. Since “015150” is the longest among the three,
# print 4 as the required answer

def solution(s, n):
    ind = {}
    mask = 0
    ind[0] = -1

    ans = 0

    for i in range(n):
        val = ord(s[i]) - ord('0')
        mask ^= (1 << val)

        if(mask in ind):
            ans = max(ans, i-ind[mask])
        else:
            ind[mask] = i
    return ans


if __name__ == "__main__":
    s = input("Enter the string: ")
    n = len(s)
    print(solution(s, n))
