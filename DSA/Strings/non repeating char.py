# this porgram will print no of non-repeating characters!
def sol(s):
    li = []
    for i in s:
        count = 0
        for j in s:
            if i == j:
                count += 1
            if count > 1:
                break
        if count == 1:
            li.append(j)
    return len(li)


s = 'instagram'
# print(sol(s))


# this program will print all non-repeating characters!

def sol(s):
    for i in s:
        count = 0
        for j in s:
            if i == j:
                count += 1
            if count > 1:
                break
        if count == 1:
            print(i, end=" ")


sol(s)
