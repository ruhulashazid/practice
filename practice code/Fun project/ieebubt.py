import turtle as t

t.penup()
t.setpos(-50,50)
t.pendown()

t.pensize(10)
t.pencolor("blue")
t.forward(100)
t.backward(100)

t.right(90)
t.forward(100)

t.left(90)
t.forward(100)
t.backward(100)
t.right(90)

t.forward(100)
t.left(90)
t.forward(100)
t.done()

#---------------------------#
import turtle
import time
t = turtle.Turtle()

def curve():
    t.pen(pencolor="white", pensize=3, speed=5)
    for i in range(200):
        t.rt(1)
        t.fd(1)
        
window = turtle.Screen()
window.bgcolor('black')
window.screensize(800, 700)
window.setup(width=1.0, height=1.0, startx=None, starty=None)


t.penup()
t.goto(-500,100)
time.sleep(1)
t.pendown()
t.shapesize(1,2,1)

# ==============="I"==================
t.pen(pencolor="white",fillcolor="blue", pensize=3, speed=8)

t.begin_fill()

t.fd(160)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(60)
t.lt(90)
# ===========Height of the 'I'=========
t.fd(140)
t.lt(90)
t.fd(60)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(160)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(60)
t.lt(90)
t.fd(140)
t.left(90)
t.fd(60)
t.rt(90)
t.fd(25)

t.end_fill()

#---------------
#

#________________
t.penup()
t.goto(-500,100)
time.sleep(1)
t.pendown()
t.shapesize(1,2,1)

# ================="E"=================

t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=8)
t.begin_fill()

t.lt(90)
t.fd(120)
t.rt(90)
t.fd(80)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(60)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(60)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(60)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(60)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(80)

t.end_fill()
# =====================================

t.penup()
t.rt(180)
#Gap between "I" and "E"
t.fd(200)
t.pendown()


# =========================================

time.sleep(2)


t.penup()
t.goto(-550,-20)
t.pendown()


