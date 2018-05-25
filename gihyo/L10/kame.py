#coding:utf-8

import turtle

class Kame(turtle.Turtle):
    def __init__(self):
        ## Call the "parent class"
        super(Kame, self).__init__()
        self.shape("turtle")
        self.shapesize(2, 2)
        self.radians()
        self.width(5)
        self.pencolor("white")
        self.getscreen().bgcolor("gray")
        self.getscreen().onclick(self.clickMove)
    def clickMove(self, x, y):
        self.goto(x, y)

