import random

m = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(random.randint(-50, 50))
    m.append(row)

sum_diag = m[0][0] + m[1][1] + m[2][2] + m[3][3] + m[4][4]
print(sum_diag)

c = 0

for row in m:
    for el in row:
        if el < 0:
            c += 1
print(c)
