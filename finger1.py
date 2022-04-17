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
        self.x = self.l1*cos(self.t1)
        self.y = self.l1*sin(self.t1)
        self.p = self.x + (self.l2*cos(self.t2))
        self.q = self.y + (self.l2*sin(self.t2))
        self.render()

    def curl(self, t1, t2=0):
        self.t1 = t1 * pi/180
        self.t2 = self.t1 + (t2 * pi/180)
        # self.joint1()
        self.s1.pos = vector(self.px, self.py, self.pz)
        # self.joint2()

        self.s2.pos = vector(self.px + self.x, self.py + self.y, self.pz)
        # self.joint3()

        self.s3 .pos = vector(self.px + self.p, self.py + self.q, self.pz)

    def render(self):
        self.joint1()
        self.cylinder1()
        self.joint2()
        self.cylinder2()
        self.joint3()

    def joint1(self):
        self.s1 = sphere(pos=vector(self.px, self.py, self.pz),
                         radius=0.25, color=color.blue)

    def cylinder1(self):

        self.c1 = cylinder(pos=vector(self.px, self.py, self.pz), size=vector(self.l1, 0, 0), axis=vector(
            self.x, self.y, 0), radius=0.1)

    def joint2(self):

        self.s2 = sphere(pos=vector(self.px + self.x, self.py + self.y,
                         self.pz), radius=0.25, color=color.blue)

    def cylinder2(self):

        self.c2 = cylinder(pos=vector(self.px + self.x, self.py + self.y, self.pz), size=vector(self.l2, 0, 0),
                           axis=vector((self.p - self.x), (self.q - self.y), 0), radius=0.1)

    def joint3(self):

        self.s3 = sphere(pos=vector(self.px + self.p, self.py + self.q,
                         self.pz), radius=0.25, color=color.blue)


def main():
    pv = vector(-2, 0, 2)
    f1 = finger(1.5, 1, -30, -10, pv)
    pv2 = vector(0, 0, 1)
    f2 = finger(2, 1, -10, -80, pv2)
    pv3 = vector(0, 0, 0)
    f3 = finger(2, 1, -10, -80, pv3)
    pv4 = vector(0, 0, -1)
    f4 = finger(2, 1, -10, -80, pv4)
    pv5 = vector(0, 0, -2)
    f5 = finger(1.5, 1, -10, -80, pv5)


main()
