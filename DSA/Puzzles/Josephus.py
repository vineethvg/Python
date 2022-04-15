# There are n people standing in a circle waiting to be executed.
# The counting out begins at some point in the circle and proceeds around the circle in a fixed direction.
# In each step, a certain number of people are skipped and the next person is executed.
# The elimination proceeds around the circle (which is becoming smaller and smaller as the executed people are removed),
# until only the last person remains, who is given freedom.
# Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle.


# The task is to choose the place in the initial circle so that you are the last one remaining and so survive.

# For example, if n = 5 and k = 2, then the safe position is 3.
# Firstly, the person at position 2 is killed, then person at position 4 is killed, then person at position 1 is killed.
# Finally, the person at position 5 is killed. So the person at position 3 survives.

# If n = 7 and k = 3, then the safe position is 4. The persons at positions 3, 6, 2, 7, 5, 1 are killed in order, and person at position 4 survives.


# =====================================================================
def Josephus(person, k, index):

    if(len(person) == 1):
        print(person[0])
        return
    index = ((index+k) % len(person))
    person.pop(index)
    Josephus(person, k, index)


n = 47
k = 5
k -= 1
index = 0

person = []
for i in range(1, n+1):
    person.append(i)
# Josephus(person, k, index)
# =====================================================================


def sol(n, k):
    if n == 1:
        return 1
    else:
        return(sol(n-1, k)+k-1) % n+1


N = 14
K = 2
# print(sol(N, K))

# =====================================================================
# when step size is fixed


def sol1(n):
    p = 1
    while p <= n:
        p *= 2

    return(2*n)-p+1


n = 16
print(sol1(n))
