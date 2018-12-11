def hourglass_check(arr, x, y):
    chkX,chkY = False,False
    if x >= 0 and x + 2 < len(arr):
        chkX = True
    if y >= 0 and y + 2 < len(arr):
        chkY = True
    if chkX and chkY:
        return True
    else:
        return False


set = """-1 -1 0 -9 -2 -2
-2 -1 -6 -8 -2 -5
-1 -1 -1 -2 -3 -4
-1 -9 -2 -4 -4 -5
-7 -3 -3 -2 -9 -9
-1 -3 -1 -2 -4 -5
"""

n = set.split("\n")
n.pop()
j = []
for i in n:
    j.append(list(map(int,i.split(" "))))
#print (j)

def hourglassSum(arr):
    mx = -60
    for x in range(len(arr)):
        for y in range(len(arr)):
            if (hourglass_check(arr, x, y)):
                a, b, c, d, e, f, g = arr[x][y], arr[x][y+1], arr[x][y+2], arr[x+1][y+1], arr[x+2][y], arr[x+2][y+1], arr[x+2][y+2]
                # print("%d,%d,%d\n" % (a, b, c))
                # print(" %d \n" % (d))
                # print("%d,%d,%d\n" % (e, f, g))
                variadd = a + b + c + d + e + f + g
                if (mx < variadd):
                    mx = variadd
    return mx

add = hourglassSum(j)
print (add)
