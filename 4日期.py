year=int(input('年：\n'))
month=int(input('月：\n'))
day=int(input('日：\n'))
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0<month<=12:
    if (year%400==0) or (year%4==0) and (year%100 != 0) and month>2:
        x = months[month - 1]+day-1
    else:
        x = months[month-1]+day
else:
    print('月份错误')
# months = (0,31,59,90,120,151,181,212,243,273,304,334)
# if 0 < month <= 12:
#     x = months[month - 1]
# else:
#     print ('data error')
# x += day
print ('这是'+str(year)+'年的第'+str(x)+'天')