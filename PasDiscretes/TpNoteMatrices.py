import numpy as np
import math as m

A = np.array(([[(m.sqrt(6)+m.sqrt(2))*0.25,(m.sqrt(2)-m.sqrt(6))*0.25],[(m.sqrt(6)-m.sqrt(2))*0.25,(m.sqrt(6)+m.sqrt(2))*0.25]]))
B = A
def Exo1(A,n):
    B = A
    for i in range(1,n):
        B = B @ A
        print(B)

print(Exo1(B,24))