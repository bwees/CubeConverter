import math


TOLERANCE = .8

# determine if a point is within a sphere
def in_sphere(x, y, z, x0, y0, z0, r):
    return (x-x0)**2 + (y-y0)**2 + (z-z0)**2 <= r**2

#determine if a point is within a cylinder
def in_cylinder(x, y, z, x0, y0, z0, r, h):
    return (x-x0)**2 + (y-y0)**2 <= r**2 and abs(z-z0) <= h

# determine if a point is within a cone
def in_cone(x, y, z, x0, y0, z0, r, h):
    return (x-x0)**2 + (y-y0)**2 <= (z-z0)**2 * (r/h)**2 and abs(z-z0) <= h

# determing if a point is in a wave
# function: sin(x+y+shift) = z
def in_wave(x, y, z, a, ha, shift, ver_shift):
    return abs(z - (a * math.sin(x/ha + y/ha + shift))-ver_shift) <= TOLERANCE

#determing if a point is in a circular wave, that looks like a drop in water
# function: sin(sqrt(x^2 + y^2)+shift) = z
def in_circular_wave(x, y, z, a, ha, shift, ver_shift):
    x -= 3.5
    y -= 3.5
    return abs(z - (a * math.sin(math.sqrt(x**2 + y**2)/ha + shift))-ver_shift) <= TOLERANCE

def in_swapped_circular_wave(x, y, z, a, ha, shift, ver_shift):
    z -= 3.5
    x -= 3.5
    return abs(y - (a * math.sin(math.sqrt(z**2 + x**2)/ha + shift))-ver_shift) <= TOLERANCE

# determing if a point is in a plane, rotated about, x and y axis
def in_plane(x_rot, y_rot):
    return abs(x_rot) <= TOLERANCE and abs(y_rot) <= TOLERANCE


# determing if a point is in a wave
# function: sin(x+y+shift) = z
def in_wave_down(x, y, z, a, ha, shift, ver_shift):
    return z - (a * math.sin(x/ha + y/ha + shift))-ver_shift <= TOLERANCE