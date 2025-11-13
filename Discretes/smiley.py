import turtle
from tkinter import mainloop

t = turtle.Turtle()

def smiley():
    #fond clair
    t.speed(0)
    t.goto(0,0)
    t.color(1,0.58,0.)
    t.begin_fill()
    t.circle(200,360)
    t.end_fill()
    t.penup()

    #fond sombre
    t.goto(0,5)
    t.pendown()
    t.color(1,0.8,0)
    t.begin_fill()
    t.circle(195,360)
    t.end_fill()
    t.penup()

#   reflet
    t.circle(195,150)
    t.color("white")
    t.pendown()
    t.circle(195,20)
    t.penup()
    t.circle(195,190)



    #bouche haut
    t.goto(100,0)
    t.color("black")
    t.left(90)
    t.circle(100,35)
    t.pendown()
    t.begin_fill()
    t.circle(100,110)
    t.penup()
    t.circle(100,35)

    #bouche bas
    t.goto(-300,345)

    t.circle(300,74)
    t.pendown()
    t.circle(300,32)
    t.penup()


    #yeux
    t.goto(0,-300)
    t.right(15)

    t.circle(300,149)
    t.pendown()
    t.circle(300,18)
    t.penup()
    t.circle(300,19)
    t.pendown()
    t.circle(300,18)
    t.penup()
    t.circle(300,1120)

    #sourcils bas
    t.goto(5,250)
    t.circle(80,239)
    t.pendown()
    t.circle(80,70)
    t.penup()
    t.circle(80,180)

    #sourcils haut
    t.goto(-48,143)
    t.circle(80,150)
    t.pendown()
    t.circle(80,67)
    t.penup()
    t.circle(80,2000)

    #oeil droit
    t.goto(55,150)
    t.right(90)
    t.circle(60,140)
    t.pendown()
    t.circle(60,80)
    t.circle(6,180)
    t.forward(20)



    mainloop()



print(smiley())