from vpython import *
from time import sleep

class finger:
    def __init__(self, l1, l2, t1, t2):
        self.l1 = l1
        self.l2 = l2
        self.t1 = t1 * pi/180
        self.t2 = self.t1 + (t2 * pi/180)
        self.render()

    def curl(self,t1,t2=0):
        self.t1 = t1 * pi/180
        self.t2 = self.t1 + (t2 * pi/180)
        #self.joint1()
        self.s1.pos = vector(0, 0, 0)
        #self.joint2()
        x = self.l1*cos(self.t1)
        y = self.l1*sin(self.t1)
        self.s2.pos = vector(x, y, 0)
        #self.joint3()
        p = x + (self.l2*cos(self.t2))
        q = y + (self.l2*sin(self.t2))
        self.s3 .pos = vector(p, q, 0)
    
    def render(self):
        self.joint1()
        self.joint2()
        self.joint3()

    def joint1(self):
        self.s1 = sphere(pos=vector(0, 0, 0), radius=0.25, color=color.blue)

    def joint2(self):
        x = self.l1*cos(self.t1)
        y = self.l1*sin(self.t1)
        self.s2 = sphere(pos=vector(x, y, 0), radius=0.25, color=color.blue)

    def joint3(self):
        x = self.l1*cos(self.t1)
        y = self.l1*sin(self.t1)
        p = x + (self.l2*cos(self.t2))
        q = y + (self.l2*sin(self.t2))
        self.s3 = sphere(pos=vector(p, q, 0), radius=0.25, color=color.blue)


def main():
    f1 = finger(4, 2, 0, 0)


main()