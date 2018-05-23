#coding:utf-8

import sys

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    add = a+b
    print("2つの引数の和は"+str(add))
except:
    print("Error!")

print("End")
