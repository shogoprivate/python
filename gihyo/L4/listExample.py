#coding:utf-8

import random

listInt = [10, 11, 12, 13]

#---------------------------
# len  
#---------------------------
lenList = len(listInt)
print("The number of elements is "+str(lenList))

#---------------------------
# append
#---------------------------
print("Before:"+str(listInt))
for i in range(20, 24, 1):
    listInt.append(i)
print("After1:"+str(listInt))

#---------------------------
# insert
#---------------------------
num = listInt.index(13)
for i in range(14, 20, 1):
    num += 1
    listInt.insert(num, i)
print("After2:"+str(listInt))


#---------------------------
# pop 
#---------------------------
for i in range(14, 20, 1):
    num = listInt.index(i)
    listInt.pop(num)
print("After3:"+str(listInt))

#---------------------------
# remove 
#---------------------------
for i in range(20, 24, 1):
    listInt.remove(i)
print("After4:"+str(listInt))

#---------------------------
# extend 
#---------------------------
listInt.extend(range(20, 24, 1))
print("After5:"+str(listInt))

#---------------------------
# sort 
#---------------------------
random.shuffle(listInt)
print("Before:"+str(listInt))
listInt.sort()
print("After1:"+str(listInt))

#---------------------------
# reverse 
#---------------------------
listInt.reverse()
print("After2:"+str(listInt))
