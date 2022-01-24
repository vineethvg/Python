# def rev(s):
#     x = ""
#     for i in s:
#         x = i + x
#     # return x

#     # return s[::-1]
#     # return "".join(reversed(s))


# s = 'abcd'
# print(rev(s))

# ==============================================================================
# Reversal of string through stack implementation
def createStack():
    stack = []
    return stack


def push(stack, item):
    stack.append(item)


def pop(stack):
    return stack.pop()


def stackRev(str):
    n = len(str)
    stack = createStack()
    for i in range(0, n, 1):
        push(stack, str[i])

    S = ""

    for i in range(0, n, 1):
        S += pop(stack)

    return S


if __name__ == '__main__':
    str = 'abcd'
    print(stackRev(str))
