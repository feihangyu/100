#输出第X个 与x个
x = int(input('输入'))
#常规方法：
def fib(x):
    a,b=0,1
    for i in range(x):
        a,b=b,a+b
        print(a)
    print(a)
fib(x)
print('=======')
#递归方法
def fib2(x):
    if x==1 or x==2:
         return 1
    return fib2(x-1)+fib2(x-2)
print(fib2(x))
print('=======')
#递归数列出来
def fib3(x):
    if x==1:
        return [1]
    if x==2:
        return [1,1]
    fibs =[1,1]
    for i in range(2,x):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs
print(fib3(x))
