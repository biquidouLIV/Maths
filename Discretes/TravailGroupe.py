import random
import turtle
import numpy as np
t = turtle.Turtle()


list=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]


def Moyenne(list):
    somme = 0
    ecart =0
    for i in range(0,len(list)):
        for j in range(0,len(list[i])):
            somme += list[i][j]

    moyenne = (somme/(len(list)*len(list[0])))

    for i in range(0,len(list)):
        for j in range(0,len(list[i])):
            ecart += ((list[i][j]-moyenne)**2)/(len(list)*len(list[0]))

    return(moyenne,ecart)



def Triangles(n):
    t.speed(0)
    for i in range(1,n+1):
        if(i%3==1):
            t.color("black")
        elif(i%3==2):
            t.color("red")
        elif(i%3==0):
            t.color("green")

        if(i%2==1):
            t.begin_fill()
            t.forward(200)
            t.left(135)
            t.forward(20000 ** (1 / 2))
            t.left(90)
            t.forward(20000 ** (1 / 2))
            t.left(135)
            t.forward(200)
            t.end_fill()
        else:
            t.begin_fill()
            t.left(45)
            t.forward(20000 ** (1 / 2))
            t.left(135)
            t.forward(200)
            t.left(135)
            t.forward(20000 ** ( 1 / 2))
            t.end_fill()
            t.left(180)
            t.forward(20000 ** ( 1 / 2))
            t.right(135)




def Graphe(n):
    Pop = [10,10,10]
    Proba = [[0,0,1],[1/3,1/3,1/3],[0,1/2,1/2]]
    for i in range(1,n):
        Pop = np.dot(Pop,Proba)
        print(Pop)

print(Triangles(3))




def GrapheProba(n):
    Pop = [10,10,10]
    Pop_avant = [10,10,10]
    Pop_apres =[10,10,10]
    for i in range(1,n+1):
        for i in range(0,Pop_avant[2]):
            a=random.random()
            if (a<0.5):
                Pop_apres[2] -= 1
                Pop_apres[1] += 1

        for i in range(0,Pop_avant[1]):
            b=random.random()
            if (b>2/3):
                Pop_apres[0] +=1
                Pop_apres[1] -=1
            elif(b<1/3):
                Pop_apres[2] += 1
                Pop_apres[1] -= 1

        for i in range(0,Pop_avant[0]):
            Pop_apres[2] += Pop_apres[0]
            Pop_apres[0] = 0
        Pop = Pop_apres
        print(Pop)

print(GrapheProba(10))


