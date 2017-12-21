#100道python练习题第一题
#1.1、2、3、4能组成多少个互不相同且无重复数字的三位数？各是多少
#分析：可填在百位，十位的数字都是1,2,3,4.组成所有后再去掉不满足的
n=1
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j and j!=k and i!=k):
                print(n)
                print (i,j,k)
                n=n+1
print(n-1)


