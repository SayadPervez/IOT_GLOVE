from vpython import *

palm = box( size=vector(1,1,0.2),                   
                   color=vector(1,0,0) )

finger1 = cylinder( size=vector(0.5,0.1,0.1), pos=vector(0,0.5,0),              
            color=vector(0,0,1),axis=vector(0,1,0) ) 

finger2 = cylinder( size=vector(0.5,0.1,0.1), pos=vector(0.2,0.5,0),              
            color=vector(0,0,1),axis=vector(0,1,0) ) 

finger3 = cylinder( size=vector(0.5,0.1,0.1), pos=vector(-0.2,0.5,0),              
            color=vector(0,0,1),axis=vector(0,1,0) ) 

#hand = compound([palm,finger3,finger2,finger1])

def invert(x):
    if(x<1):
        return(x+0.1)
    else:
        return(0)

import time

s = 0.5
while(True):
    finger1.size=vector(s,0.1,0.1)
    #print("hi")
    s+=0.1
    time.sleep(1)