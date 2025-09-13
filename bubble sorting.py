import random
import array as arr
a = arr.array('i', [])
for i in range(15):
    b = random.randint(0, 100)
    a.append(b)
memo = 0
num = len(a)-1

for i in range(0, num):
  num_it_2 = num - i
  for j in range(0, num_it_2):
    if a[j]>a[j+1]:
        memo = a[j]
        a[j] = a[j+1]
        a[j+1] = memo
print(a)
