import random
import turtle
t = turtle.Turtle()

def dessin1():
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.circle(100,180)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)

def dessin2():
    t.forward(200)
    t.left(135)
    t.forward(20000**(1/2))
    t.left(90)
    t.forward(20000**(1/2))
    t.left(135)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(135)
    t.forward(20000**(1/2))
    t.left(135)
    t.forward(100)
    t.left(135)
    t.forward(20000**(1/2))
    t.left(135)
    t.forward(100)
    t.left(45)
    t.circle((20000**(1/2))/2,180)

def dessin3():
    t.left(90)
    t.circle(50,-180)
    t.left(180)
    t.circle(50,180)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.circle(-100,180)
    t.forward(50)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(300)

def dessin4(n):
    for i in range(0,n):
        if(i%2==0):
            t.color("blue")
        else:
            t.color("black")
        t.begin_fill()
        for j in range(0,4):
            t.forward(100)
            t.left(90)
        t.forward(100)
        t.end_fill()


def dessin5(n):
    for i in range(0,n):
        if(i%2==0):
            t.begin_fill()
            t.color("blue")
            t.forward(100)
            t.left(90)
            t.circle(50,180)
            t.left(90)
            t.forward(100)
            t.end_fill()
        else:
            t.begin_fill()
            t.color("red")
            t.forward(100)
            t.right(90)
            t.circle(-50,180)
            t.right(90)
            t.forward(100)
            t.end_fill()

def dessin6(n):
    for i in range(1,n+1):
        for j in range(0,4):
            t.forward(50*i)
            t.left(90)

def dessin7(n):
    for i in range(1,n):
        t.penup()
        t.goto(0,-50*i)
        t.pendown()
        t.circle(50*i,360)

def dessin8(n):
    t.speed(0)
    i=n
    while(i!=0):
        if(i%2==1):
            t.color("blue")
        else:
            t.color("black")
        t.begin_fill()
        for j in range(0,4):
            t.forward(50*i)
            t.left(90)
        t.end_fill()
        i-=1

def dessin9(n):
    t.speed(0)
    for k in range(1,n+1):
        for i in range(0,n):
            t.color(random.random(),random.random(),random.random())
            t.begin_fill()
            for j in range(0, 4):
                t.forward(50)
                t.left(90)
            t.forward(50)
            t.end_fill()
        t.penup()
        t.goto(0,50*k)
        t.pendown()

print(dessin2())