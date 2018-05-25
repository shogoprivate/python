#coding:utf-8

import random

class Dice:
    def __init__(self, val=6):
        if val in [4, 6, 8, 12, 20]:
            self.faceNum = val
        else:
            raise ValueError("そのような多面体は存在しません．")
            #raise Exception("そのような多面体は存在しません．")
    def shoot(self):
        return random.randint(1,self.faceNum)

# The name of a "initialized method" is "__init__"
# The name of a instance is automatically assigned to "self"
