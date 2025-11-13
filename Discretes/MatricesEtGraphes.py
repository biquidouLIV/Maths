import locale
import random

import numpy as np
from numpy.ma.core import append


def exo1(a,b,c,d):
    return [a,b],[c,d]

def exo2(a,b,c,d,e,f,g,h):
    return([a+e,b+f],[c+g,d+h])

def exo3(a,b,c,d,e,f,g,h):
    return([a*e+b*g,a*f+b*h],[c*e+d*g,c*f+d*h])

def exo4(a,b,c,d):
    return([a*a+b*c,a*b+b*d],[c*a+d*c,c*b+d*d])


def exo5(a,b,c,d,n):
    M = np.array([[a,b],[c,d]])
    N = M
    for i in range(1,n):
        M= M@N
    return(M)

def exo6(n):
    M=[]
    L=[]
    for i in range (1,n+1):
        for j in range(1,n+1):
            if (i!=j):
                L.append(0)
            else:
                L.append(1)
        M.append(L)
        L=[]
    return(M)

M=[[1,2,3,4,5,6],[2,1,2,3,4,5],[3,2,1,2,3,4],[4,3,2,1,2,3],[5,4,3,2,1,2],[6,5,4,3,2,1]]
def exo7():
    I = exo6(len(M))
    for i in range(0,len(I)):
        M[i][i] += I[i][i]
    return(M)



def exo8():
    for i in range(0,len(M)):
        M[i][i]=0
    return(M)


def exo9():
    for i in range(1,len(M)):
        for j in range(0,len(M)):
            if (M[i][j] != M[j][i]):
                return("pas symétrique")
    return("symétrique")


def exo10():
    minValue = M[0][0]
    for i in range(0,len(M)):
        for j in range(0, len(M)):
            if (M[i][j] < minValue):
                minValue = M[i][j]
    return(minValue)

def exo13(n):
    value = 1
    for i in range(1,n):
        value *= i
    return(value)

def exo14(k,n):
    return(exo13(n)/(exo13(n-k)*exo13(k)))




#def exo15(k,n):
#    for i in range(0,n):

def exo16(n):
    Pop = [100,20]
    Prob = [[0.5,0.5],[0,1]]
    for i in range (1,n+1):
        Pop = ([Pop[0]*Prob[0][0]+Pop[1]*Prob[1][0],Pop[0]*Prob[0][1]+Pop[1]*Prob[1][1]])
    return(Pop)


def exo17(n):
    Pop = [100,20]
    for i in range(1,n+1):
        for i in range(0,Pop[0]):
            a=random.random()
            if (a<0.5):
                Pop[0] -= 1
                Pop[1] += 1
        print(Pop)

def exo18(n):
    Pop = [100,20]
    for i in range(1,n+1):
        for i in range(0,Pop[0]):
            a=random.random()
            if (a<0.5):
                Pop[0] -= 1
                Pop[1] += 1
        for i in range(0,Pop[1]):
            b=random.random()
            if (b>0.90):
                Pop[0] +=1
                Pop[1] -=1
        print(Pop)



def exo19():
    position = 1
    i = 0
    L=[]
    while(position !=3):
        if(position==1):
            a = random.random()
            if (a > 0.70):
                position = 2
        elif(position==2):
            b = random.random()
            if(b >= 0.70):
                position = 3
            elif(b<0.60):
                position = 1
            elif(0.60 <= b < 0.70):
                position=2
        i += 1
        L.append(position)
    return(i,L)





def exo20():
    position = 1
    rep=500
    i = 0
    sum = 0
    for i in range(0,rep):
        while(position !=3):
            if(position==1):
                a = random.random()
                if (a > 0.70):
                    position = 2
            elif(position==2):
                b = random.random()
                if(b >= 0.70):
                    position = 3
                elif(b<0.60):
                    position = 1
                elif(0.60 <= b < 0.70):
                    position=2
            i+=1
    return(i)

print(exo20())






