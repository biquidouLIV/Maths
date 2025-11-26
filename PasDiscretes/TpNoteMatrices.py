from symtable import Class

import numpy as np
import math as m
import matplotlib.pyplot as plt

A = [[(m.sqrt(6)+m.sqrt(2))*0.25,(m.sqrt(2)-m.sqrt(6))*0.25],
     [(m.sqrt(6)-m.sqrt(2))*0.25,(m.sqrt(6)+m.sqrt(2))*0.25]]
B = A
I = [[1,0],[0,1]]


def ProduitMatriciel(M,N):
    return ([M[0][0]*N[0][0] + M[0][1]*N[1][0],
            M[0][0]*N[0][1] + M[0][1]*N[1][1]],
            [M[1][0]*N[0][0] + M[1][1]*N[1][0],
             M[1][0]*N[0][1] + M[1][1]*N[1][1]])

def TestIdentite(M):
    tol = 0.00001
    if (abs(M[0][0] - 1) < tol and abs(M[1][1] - 1) < tol and abs(M[0][1]) < tol and abs(M[1][0]) < tol):
        return True


def Exo1(A):
    B = A
    n = 1 #n = 1 car A = A^1
    while not TestIdentite(B):
        B = ProduitMatriciel(B,A)
        n += 1
    print("n =",n)

def Exo5():
    Mmax = np.array([50,20,30,5])
    Mactu = np.array([35,20,10,2])
    Poids = np.array([0.1,0.2,0.3,1])
    Puissance = np.array([10,8,20,17])

    PoidsMax = Mmax.dot(Poids)
    PoidsActu = Mactu.dot(Poids)
    PuissanceFeu = Mactu.dot(Puissance)



    print("Poids Max =",PoidsMax,"Poids Actuel =",PoidsActu, "puissance de feu =",PuissanceFeu)



def Exo6():
    Stats = np.array([
             [48.20,75,107,100,63,63,72,65],
             [63.38,58,91,82,74,52,65,45],
             [43.38,64,100,91,57,57,72,72],
             [39.52,85,75,107,52,74,59,50]])         #j'ai divisé les pv par 100

    classe = np.array([
             [0,0,1,0],  # PV
             [0,1,0,0],  # PM
             [1,0,0,0],  # Force
             [0,1,0,0],  # Magie
             [0,0,1,0],  # Constitution
             [1,0,0,0],  # Esprit
             [0,0,0,1],  # Chance
             [0,0,0,1]   # Rapidité
      # guerrier / mage / tank /voleur
    ])

    perf = Stats.dot(classe)
    print(perf)

def Exo7():
    M = np.array([[0,10,10,0,0],
                  [0,0,10,10,0]
                  ])
    plt.plot(M[0],M[1])


    symetrie = np.array([[-1,0],
                         [0,1]])
    homothetie = np.array([[2,0],
                           [0,2]])  #*2
    rotation = np.array([[0,-1],
                         [1,0]])    #pi/2

    M =symetrie.dot(M)
    M =homothetie.dot(M)
    M =rotation.dot(M)

    plt.plot(M[0],M[1])
    plt.show()


    return M

#print(Exo1(A))
#print(Exo5())
print(Exo6())
#print(Exo7())

