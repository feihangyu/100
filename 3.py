# 题目 ：求一个整数，它加上100和加上268后都是一个完全平方数
import math
type= print(type(2*3))
for x in range(-100,10000):#哈哈，标准答案不准确
    a=int(math.sqrt(x+268))
    b=int(math.sqrt(x+100))
    # if (type(a*b)==type)==True:   这样判断报错
    # if isinstance(a,int):
    #     print(x)   这样判断也不行
    if a*a==(x+268)and b*b==(x+100):
        print(x)

