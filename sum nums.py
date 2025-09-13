a = input("5tyznachne chyslo")
b = list(a)
for i in range(0, 5):
    b[i] = int(b[i])
s = sum(b)
print(s)
