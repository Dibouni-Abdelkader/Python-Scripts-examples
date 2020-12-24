from turtle import*
def triangle(a,b,c):
    for i in range(3):
        color(a)
        forward(b)
        left(c)

#triangle('blue',300,150)



def triangle2():
    up()
    goto(0,0)
    down()
    triangle("green",200,200)


triangle2()


def triangle3():
    up()
    goto(0,0)
    down()
    triangle2()

triangle3()

    
def triangle4():
    
    up()
    backward(200)
    down()
    triangle3()

triangle4()
