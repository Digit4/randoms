inp = """5 4
1 2 3 4 5
"""

n = inp.split("\n")
n.pop()
Q = []
for i in n:
    Q.append(list(map(int, i.split(" "))))
print(Q)

def leftRotation(arr,rot):
	