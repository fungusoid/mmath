import math

def radians_to_degrees(f):
    # return (f / (2.0 * math.pi)) * 360.0
    return math.degrees(f)

def degrees_to_radians(f):
    # return (f / 360.0) * (2.0 * math.pi)
    return math.radians(f)

def is_zero(f):
    return math.isclose(f, 0.0)