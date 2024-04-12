import math
from mmath import *
from vec4 import *

# plane

class plane:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def normal(self):
        return vec4(self.a, self.b, self.c, 0.0)

    def side(self, p):
        f = self.a * p.x + self.b * p.y + self.c * p.z + self.d
        if is_zero(f):
            return 0
        elif f > 0.0:
            return 1
        else:
            return -1

def plane_from_normal_and_point(n, p):
    n = n.unit() # not necesary
    return plane(n.x, n.y, n.z, -(n.x * p.x + n.y * p.y + n.z * p.z))

# sphere

class sphere:
    def __init__(self, c, r):
        self.center = c
        self.radius = r

    def side(self, p):
        f = p.sub(self.center).length() - self.radius
        if is_zero(f):
            return 0
        elif f > 0.0:
            return 1
        else:
            return -1

# triangle

class triangle:
    def __init__(self, v0, v1, v2):
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2

    def normal(self):
        return self.v2.sub(self.v0).cross(self.v1.sub(self.v0))
    
    def plane(self):
        return plane_from_normal_and_point(self.normal(), self.v0)
    
    def side(self, p):
        return self.plane().side(p)
