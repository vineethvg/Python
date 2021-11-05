def convert(s, numRows):

    # if one row is present return the string
    if numRows == 1:
        return s

    rows = ["" for i in range(numRows)]
    direction = -1
    row = 0

    for i in range(len(s)):
        rows[row] = rows[row]+s[i]
        if (row == 0 or row == numRows-1):
            direction = direction * -1
        row = row + direction

    return "".join(rows)


s = "PAYPALISHIRING"
numRows = 3
x = convert(s, numRows)
print(x)
