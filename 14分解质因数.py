#分解质因数
x=int(input())
c=[]
for a in range(2,int(x/2)):
    if x%a==0:
        c.append(a)
        print(a)
        
    #     b=x/a
    #     x=b
    # else:
    #     print('是质数')
    # break
# print(b)