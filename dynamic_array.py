inp = """2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1
"""

n = inp.split("\n")
n.pop()
Q = []
for i in n:
    Q.append(list(map(int, i.split(" "))))

lastAnswer = 0
