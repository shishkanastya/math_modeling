a = 3
b = 'Good'
c = ['Bad', 4, 'Petya molodec']

earth_mass = 5.972237 * 10 **30
sigma_steff_balc = 5.67036713 * 10 ** (-8)
gravity_constant = 6.67488 * 10 ** (-11)

import lec_3_shishkanastya_scene

print(lec_3_shishkanastya_scene.a)

b = lec_3_shishkanastya_scene.b * 3
print(b)

print(lec_3_shishkanastya_scene.c[2])

import lec_3_shishkanastya_scene as mm

print(mm.a)

b = mm.b * 3
print(b)

print(mm.c[2] * b * mm.c[0])

from lec_3_shishkanastya_scene import a, b

print(a * b)

from lec_3_shishkanastya_scene import *

print(c[2] * c[1])

from lec_3_shishkanastya_scene import earth_mass as em
from lec_3_shishkanastya_scene import gravity_constant as G
from lec_3_shishkanastya_scene import sigma_steff_bolc as sigma

g = 500 * G / 10 ** 2
print(g)

x = em * G * sigma
print(x)

from lec_3_shishkanastya_scene import b
from lec_3_import_as import b

print(b)

import lec_3_shishkanastya_scene as mm
import lec_3_import_as as l3

print(mm.b + l3.b)

import math

a = math.sin(3 * math.pi / 5)
print(a)

b = math.sqrt(3)
print(b)

c = math.log10(42)
print(c)

d = math.asin(math.tan(math.pi / 4)) * 100 / math.pi
print(d)

import numpy as np

a = [1, 2, 4]

b = np.array(a)

print(type(a))
print(type(b))

print(b * b)
print(b / b)
print(b - b)

print(b[-1])

import numpy as np

a = np.xeros((2, 3))
print(a)

a[0, 2] = 5
print(a)

b = np.ones((3, 2))
print(b)

c = np.ndarray((3, 3))
print(c)

print(type(a), type(b), type(c))

import numpy as np

a = range(0, 5, 1)
print(a)

# a = range(0, 10, 0,1)

b = np.arange(0, 5, 0,1)
print(b)

d = np.linspace(0, 5, 10)
print(d)

import numpy as np

a = [1, 5, 3, 6]
slice = a[0:2:1]
print(slice)

slice = a[3:0:-1]
print(slice)

b = np.array([a, np.array(a) * 3])
print(b)

slice = b[::, 1]
print(slice)

slice = b[1, 2:3:1]
print(slice)

slice = b[1, 2::1]
print(slice)
