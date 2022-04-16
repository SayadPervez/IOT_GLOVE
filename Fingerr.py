from vpython import *


class finger(object):
    def __init__(self, l1, l2, t1, t2):
        self.l1 = l1
        self.l2 = l2
        self.t1 = t1 * pi/180
        self.t2 = self.t1 + (t2 * pi/180)

    # def __init__(self, t1, t2):
        #self.t1 = t1
        #self.t2 = t2

    # def __init__(self, t1):
        #self.t1 = t1
       # self.t2 = t1


class joint(finger):

    def joint1(self):
        self.s1 = sphere(pos=vector(0, 0, 0), radius=0.25, color=color.blue)

    def joint2(self):
        x = self.l1/cos(self.t1)
        y = self.l1/sin(self.t1)
        self.s2 = sphere(pos=vector(x, y, 0), radius=0.25, color=color.blue)

    def joint3(self):
        x = self.l1/cos(self.t1)
        y = self.l1/sin(self.t1)
        p = x + (self.l2/cos(self.t2))
        q = y + (self.l2/sin(self.t2))
        self.s3 = sphere(pos=vector(p, q, 0), radius=0.25, color=color.blue)


def main():
    fin = joint(4, 2, 10, 10)
    fin.joint1()
    fin.joint2()
    fin.joint3()


main()
