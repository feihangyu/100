import time
myD = {1: 1,2: 'b',3: 'c'}
print (dict.keys(myD))
print (myD.values())
print (myD.items())
for key,value in myD.items():
    print (key,value)
    time.sleep(2)

