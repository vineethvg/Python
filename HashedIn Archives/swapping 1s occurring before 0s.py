# Python program for the above approach

def isBinaryStringsEqual(list1, list2):

    str1 = list(list1)
    str2 = list(list2)

    str1Zeros = 0
    str1Ones = 0

    str2Zeros = 0
    str2Ones = 0
    flag = 0

    curStr1Ones = 0

    for i in range(len(str1)):
        if (str1[i] == '1'):
            str1Ones += 1
        elif (str1[i] == '0'):
            str1Zeros += 1
        if (str2[i] == '1'):
            str2Ones += 1
        elif (str2[i] == '0'):
            str2Zeros += 1

    if (str1Zeros != str2Zeros and str1Ones != str2Ones):
        print("Not Possible")
    else:
        for i in range(len(str1)):

            if (str1[i] != str2[i]):

                if (str1[i] == '0' and curStr1Ones > 0):
                    str1[i] = '1'
                    curStr1Ones -= 1

                if (str1[i] == '0' and curStr1Ones == 0):
                    flag += 1
                    break

                if (str1[i] == '1' and str2[i] == '0'):
                    str1[i] = '0'
                    curStr1Ones += 1

        if (flag == 0):
            print("Possible")

        # Prnot possible
        else:
            print("Not Possible")

# Driver Code


# Given Strings
str1 = "0110"
str2 = "0011"

# Function Call
isBinaryStringsEqual(str1, str2)
