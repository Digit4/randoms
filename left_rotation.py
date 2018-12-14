inp = """5 4
1 2 3 4 5
"""

n = inp.split("\n")
n.pop()
Q = []
for i in n:
    Q.append(list(map(int, i.split(" "))))
#print(Q)
nd = inp.split()

n = int(nd[0])

d = int(nd[1])

a = list(map(int, inp.rstrip().split()))

print(a)


def leftRotation(arr, rot):
    new_array, l = [], len(arr)
    mov_index = rot
    for i in range(l):
        new_array.append(arr[mov_index % l])
        mov_index += 1
    res = ""
    for i in range(l):
        res += str(new_array[i]) + " "
    return res

print(leftRotation(Q[1], 4))
