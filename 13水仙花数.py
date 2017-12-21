#打印所有的水仙花数

for i in range (100,1001):
    a=int(i/100)
    b=int(i/10)%10
    c=i%10
    if a**3+b**3+c**3==i:
        print(i)