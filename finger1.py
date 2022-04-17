import time
from vpython import *
from time import sleep


def vectorParser(vec):
    print(f"Vector : {vec}")
    return(list(map(float, ((str(vec).replace("<", "")).replace(">", "")).split(","))))


class finger:

    def __init__(self, l1, l2, t1, t2, pv):
        self.l1 = l1
        self.l2 = l2
        self.t1 = t1 * pi/180
        self.t2 = self.t1 + (t2 * pi/180)
        self.px, self.py, self.pz = vectorParser(pv)
        self.render()

    def curl(self, t1, t2=0):
        self.t1 = t1 * pi/180
        self.t2 = self.t1 + (t2 * pi/180)
        # self.joint1()
        self.s1.pos = vector(self.px, self.py, self.pz)
        # self.joint2()
        x = self.l1*cos(self.t1)
        y = self.l1*sin(self.t1)
        self.s2.pos = vector(self.px + x, self.py + y, self.pz)
        # self.joint3()
        p = x + (self.l2*cos(self.t2))
        q = y + (self.l2*sin(self.t2))
        self.s3 .pos = vector(self.px + p, self.py + q, self.pz)

    def render(self):
        self.joint1()
        self.joint2()
        self.joint3()

    def joint1(self):
        self.s1 = sphere(pos=vector(self.px, self.py, self.pz),
                         radius=0.25, color=color.blue)

    def joint2(self):
        x = self.l1*cos(self.t1)
        y = self.l1*sin(self.t1)
        self.s2 = sphere(pos=vector(self.px + x, self.py + y,
                         self.pz), radius=0.25, color=color.blue)

    def joint3(self):
        x = self.l1*cos(self.t1)
        y = self.l1*sin(self.t1)
        p = x + (self.l2*cos(self.t2))
        q = y + (self.l2*sin(self.t2))
        self.s3 = sphere(pos=vector(self.px + p, self.py+q,
                         self.pz), radius=0.25, color=color.blue)


def main():
    pv = vector(0, 0, 2)
    f1 = finger(1.5, 1, -30, -10, pv)
    pv2 = vector(0, 0, 1)
    f2 = finger(2, 1, -10, -80, pv2)
    pv3 = vector(0, 0, 0)
    f3 = finger(2, 1, 90, 0, pv3)
    pv4 = vector(0, 0, -1)
    f4 = finger(2, 1, -10, -80, pv4)
    pv5 = vector(0, 0, -2)
    f5 = finger(1.5, 1, -10, -80, pv5)


main()
