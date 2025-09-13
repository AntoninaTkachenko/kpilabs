ar = input("spysok cherez probil:")
l = ar.split(" ")
vid_count = 0

for i in range(len(l)):
    l[i] = int(l[i])
    if l[i]<0:
        l[i] = l[i]**2
    else:
        vid_count += 1

if vid_count == 0:
    print("all > 0")
else:
    print(l)
