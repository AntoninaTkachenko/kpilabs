a = int(input("number:"))
b = 0
for i in range(1, a):
    if i % 5 != 0:
        b += i
    else:
        pass
print(b)