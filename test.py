import time
from vpython import *

f1_1x,f1_1y,f1_1z = 0,0,0
f1_2x,f1_2y,f1_2z = 1,0,0
f1_3x,f1_3y,f1_3z = 2,0,0

pt1 = sphere( size=vector(0.15,0.15,0.15),color=vector(0,0,1),pos=vector(f1_1x,f1_1y,f1_1z) ) # 0,0,0

pt2 = sphere( size=vector(0.15,0.15,0.15),color=vector(0,0,1),pos=vector(f1_2x,f1_2y,f1_2z) ) # 1,0,0

pt3 = sphere( size=vector(0.15,0.15,0.15),color=vector(0,0,1),pos=vector(f1_3x,f1_3y,f1_3z) ) # 2,0,0



def vectorParser(vec):
    print(f"Vector : {vec}")
    return(list(map(float,((str(vec).replace("<","")).replace(">","")).split(","))))

for _ in range(1,100):
    a,b,c = (vectorParser(pt2.pos))
    print(f"Pt2 : {a,b,c}")
    pt2.pos = vector(a-0.02,b-0.02,c)

    x,y,z = (vectorParser(pt3.pos))
    print(f"Pt3 : {x,y,z}")
    pt3.pos = vector(x-0.06,y-0.1,z)
    time.sleep(1)