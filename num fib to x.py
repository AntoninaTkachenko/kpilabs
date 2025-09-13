a = 0
b = 1
lim = int(input("do chysla:"))
mem = 0
while a < lim:
    print(a)
    mem = a
    a = b
    b += mem
