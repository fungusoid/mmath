import math
from mmath import *

class vec4:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z}, {self.w})"
    
    def vec(self):
        return vec4(self.x, self.y, self.z, 0.0)
    
    def point(self):
        return vec4(self.x, self.y, self.z, 1.0)

    def neg(self):
        return vec4(-self.x, -self.y, -self.z, self.w)
    
    def add(self, other):
        return vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def sub(self, other):
        return vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
    
    def mul(self, s):
        return vec4(self.x * s, self.y * s, self.z * s, self.w)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return vec4(x, y, z, 0.0)
    
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    
    def unit(self):
        l = self.length()
        if (is_zero(l)):
            return vec4(0.0, 0.0, 0.0, self.w)
        else:
            return self.mul(1.0 / l)

    def angle(self, other):
        l = self.length() * other.length()
        if (is_zero(l)):
            return 0.0
        else:
            return math.acos(self.dot(other) / l)

    def distance(self, other):
        return other.sub(self).length()
