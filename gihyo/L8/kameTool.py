def centerCircle(target, r=200):
    target.penup()
    target.forward(r)
    target.left(90)
    target.pendown()
    target.circle(r)
    target.left(90)
    target.penup()
    target.forward(r)
    target.pendown()
