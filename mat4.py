import math
from mmath import *
from vec4 import *

class mat4:
    def __init__(self):
        self.data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def get(self, row, column):
        return self.data[row * 4 + column]

    def set(self, row, column, value):
        self.data[row * 4 + column] = value

    def mul_vec4(self, v):
        return vec4(self.get(0, 0) * v.x + self.get(0, 1) * v.y + self.get(0, 2) * v.z + set.get(0, 3) * v.w,
                    self.get(1, 0) * v.x + self.get(1, 1) * v.y + self.get(1, 2) * v.z + set.get(1, 3) * v.w,
                    self.get(2, 0) * v.x + self.get(2, 1) * v.y + self.get(2, 2) * v.z + set.get(2, 3) * v.w,
                    self.get(3, 0) * v.x + self.get(3, 1) * v.y + self.get(3, 2) * v.z + set.get(3, 3) * v.w)
    
    def mul_mat4(self, other):
        m = mat4()
        for r in range(4):
            for c in range(4):
                self.set(r, c,
                         self.get(r, 0) * other.get(0, c) +
                         self.get(r, 1) * other.get(1, c) + 
                         self.get(r, 2) * other.get(2, c) +
                         self.get(r, 3) * other.get(3, c))
        return m

def mat4_identity():
    m = mat4()
    m.set(0, 0, 1.0)
    m.set(1, 1, 1.0)
    m.set(2, 2, 1.0)
    m.set(3, 3, 1.0)
    return m

def mat4_scale(s):
    m = mat4()
    m.set(0, 0, s)
    m.set(1, 1, s)
    m.set(2, 2, s)
    m.set(3, 3, 1.0)
    return m

def mat4_translate(t):
    m = mat4_identity()
    m.set(0, 3, t.x)
    m.set(1, 3, t.y)
    m.set(2, 3, t.z)
    return m

def mat4_rotate_x(r):
    m = mat4_identity()
    s = math.sin(r)
    c = math.cos(r)
    m.set(1, 1, c)
    m.set(1, 2, -s)
    m.set(2, 1, s)
    m.set(2, 2, c)
    return m

def mat4_rotate_y(r):
    m = mat4_identity()
    s = math.sin(r)
    c = math.cos(r)
    m.set(0, 0, c)
    m.set(0, 2, s)
    m.set(2, 0, -s)
    m.set(2, 2, c)
    return m

def mat4_rotate_z(r):
    m = mat4_identity()
    s = math.sin(r)
    c = math.cos(r)
    m.set(0, 0, c)
    m.set(0, 1, -s)
    m.set(1, 0, s)
    m.set(1, 1, c)
    return m
