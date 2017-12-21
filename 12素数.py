#素数（101，200）
import math
print(int(12.90877))
a=0
loop = 1
for i in range(101,201):
    k=int(math.sqrt(i))
    for j in range(2,k+1): #这里要注意+1 ， int是取整
        if i%j==0:
            loop = 0
            break
    if loop == 1:
        print(i)
        a+=1
    loop = 1
print('%d个' %a)
print(int(math.sqrt(121)))