#coding:utf-8

### tuple
### Read only ("tuple" can not be rewrite)
tupleExp = (1, 2, 3, '100yen')
print(tupleExp)
print(tupleExp[2:])


### set 
### Conbine same values into one value
listInt = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
print("list:"+str(listInt))
setInt = set(listInt)
print("set:"+str(setInt))
