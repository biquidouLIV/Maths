import random


def exo1(a,b,c,d):
    return(a*d-b*c)

def exo2(a,b,c,d,e,f,g,h,i):
    return(a*exo1(e,f,h,i)-b*exo1(d,f,g,i)+c*exo1(d,e,g,h))



def exo3(list):
    taille = len(list)
    if(taille==4):
        if(exo2(list[0], list[1], list[2], list[3])==0):
            return("Matrice 3*3 n'a pas de solution")
        else:
            return("kaka 3*3")
    elif(taille==9):
        if(exo1(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8])==0):
            return ("Matrice 2*2 n'a pas de solution")
        else:
            return ("kaka 2*2")





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

print(Moyenne(list))