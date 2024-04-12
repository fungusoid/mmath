import math
from mmath import *
from vec4 import *

class ray:
    def __init__(self, o, d):
        self.origin = o
        self.direction = d

    def at(self, f):
        return self.origin.add(self.direction.mul(f))

    def normalized(self):
        return ray(self.origin, self.direction.unit())

def ray_from_points(a, b):
    return ray(a, b.sub(a))

# intersection tests

class intersection:
    def __init__(self, r, p, n, uv):
        self.ray_parameter = r
        self.position = p
        self.normal = n
        self.uv = uv

def ray_plane_intersection(r, p):
    n = p.normal()
    f = n.dot(r.direction)
    if is_zero(f):
        return None
    rp = (-p.d - n.dot(r.origin)) / f
    if (rp <= 0.0):
        return None
    else:
        return intersection(rp, r.at(rp), n, None)

def ray_sphere_intersection(r, s):
    l = s.center.sub(r.origin)
    x = l.dot(r.direction)
    ll = l.dot(l)
    rr = s.radius * s.radius
    if (x < 0) and (ll > rr):
        return None
    mm = ll - x * x
    if mm > rr:
        return None
    q = math.sqrt(rr - mm)
    if ll > rr:
        t = x - q
    else:
        t = x + q
    p = r.at(t)
    return intersection(t, p, p.sub(s.center).unit(), None)

def ray_triangle_intersection(r, t):
    e1 = t.v1.sub(t.v0)
    e2 = t.v2.sub(t.v0)
    q = r.direction.cross(e2)
    a = e1.dot(q)
    if is_zero(a):
        return None
    f = 1.0 / a
    s = r.origin.sub(t.v0)
    u = f * s.dot(q)
    if u < 0:
        return None
    x = s.cross(e1)
    v = f * r.direction.dot(x)
    if (v < 0.0) or ((u + v) > 1.0):
        return None
    rp = f * e2.dot(x)
    return intersection(rp, r.at(rp), t.normal().unit(), (u, v))