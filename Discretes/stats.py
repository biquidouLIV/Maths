import random
import turtle as t

valeur = [2, 3, 4, 6,]
effectif = [3, 1, 1, 2]
def moyenne():
    somme = 0
    N = 0
    moyenne = 0
    for i in range(len(valeur)):
        N += effectif[i]

    for i in range(len(valeur)):
        somme += valeur[i]*effectif[i]
    moyenne = somme/N

    print("moyenne=",moyenne,"N=",N)

def Variance():
    N = 0
    var=0
    somme = 0
    moyenne = 0

    for i in range(len(valeur)):
        N += effectif[i]

    for i in range(len(valeur)):
        somme += valeur[i]*effectif[i]
    moyenne = somme/N

    for i in range(len(valeur)):
        var +=  (effectif[i] * ((valeur[i]-moyenne)**2)) / N

    return var

def Ecart():
    e=(Variance())**(1/2)
    print("Ecart =",e)


def Mode():
    effectifMax = effectif[0]
    k = 0
    for i in range(len(valeur)):
        if effectif[i] > effectifMax:
            effectifMax = effectif[i]
            k = i
    return(valeur[k])



## def Mediane():
    L =[1,2,3,4,5]
    med =0
    pos=0
    if len(L) % 2 == 1:
        pos= (len(L) - 1)/2
        med = L[pos]
    return med

def diagramme():
    N=0
    L = []
    for i in range(len(valeur)):
        N += effectif[i]

    for i in range(len(valeur)):
        angle  = (effectif[i]/N)*360
        L.append(angle)
    for i in range(len(L)):
        t.pensize(10)
        t.circle(100, L[i])
        t.color(random.random(),random.random(),random.random())




def diagramme2():
    N=0
    L = []
    for i in range(len(valeur)):
        N += effectif[i]

    for i in range(len(valeur)):
        height  = (effectif[i]/N)*360
        L.append(height)
        print(L)

    for i in range(len(L)):
        t.pendown()
        t.begin_fill()
        t.forward(50)
        t.left(90)
        t.forward(L[i])
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(L[i])
        t.left(90)
        t.penup()
        t.end_fill()
        t.forward(70)
        t.color(random.random(),random.random(),random.random())













