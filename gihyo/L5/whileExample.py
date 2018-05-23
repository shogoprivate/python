#coding:utf-8

import random

randNum = 0

while randNum != 4:
    randNum = random.randint(0,6)
    print(randNum)

print("Other method")

while True:
    randNum = random.randint(0,6)
    print(randNum)
    if randNum == 4:
        break
    else:
        continue

