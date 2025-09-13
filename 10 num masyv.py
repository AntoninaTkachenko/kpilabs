ar = []
for i in range(10):
    num = int(input("num"))
    ar.append(num)

u = list(set(ar))
u.sort()
if len(u) >= 2:
    num2 = u[-2]
    print(num2)

if len(set(ar)) == len(ar):
    print("yes")
else:
    print("no")
