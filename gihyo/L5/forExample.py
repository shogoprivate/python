#coding:utf-8

### for statement

#---------------------------
# with using "list-type" 
#---------------------------
listTohoku = [5349, 5478, 5344, 4644, 4968, 6259]
listShikoku = [3148, 2991, 2966, 2457]

sumCost = 0
cnt = 0

for cost in listTohoku:
    sumCost += cost
    cnt += 1

avgTohoku = float(sumCost)/cnt
sumCost = 0
cnt = 0

for cost in listShikoku:
    sumCost += cost
    cnt += 1

avgShikoku = float(sumCost)/cnt

print("Average of Tohoku:"+str(avgTohoku))
print("Average of Shikoku:"+str(avgShikoku))

#---------------------------
# with using "dict-type" 
#---------------------------
dictTohoku = {"aomori":5349,\
            "akita":5478,\
            "sendai":5344,\
            "yamagata":4644,\
            "fukushima":4968,\
            "morioka":6259}

sumCost = 0
cnt = 0

for cost in dictTohoku:
    sumCost += dictTohoku[cost]
    cnt += 1

avgTohoku = float(sumCost)/cnt
print("Average of Tohoku:"+str(avgTohoku))

# *The order of keys in dict-type is not determined
