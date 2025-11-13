def exo1(n):
    i=1
    while 2**i<n:
        i=i+1
    return(i)
print(exo1(7))


def exo2(n,m):
    i=1
    while m**i<n:
        i=i+1
    return(i)
print(exo2(120,2))

def exo3(n,m):
    L=[]
    for i in range (2,m):
        L.append(exo2(n,i))
    return(L)
print(exo3(120,4))

#def exo4(a,b):
#    for

def exo6(n):
    L=list(map(int, str(n)))
    L2=[]
    i=0
    while i != len(L):
        i=i+1
        L2.append(L[i])
    return(L,L2)

print(exo6(123))