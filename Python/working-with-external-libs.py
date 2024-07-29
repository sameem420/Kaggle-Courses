# Imports

import math

print("It's math! It has type {}".format(type(math)))

# print(dir(math))

print("pi to 4 significant digits = {:.4}".format(math.pi))

print(math.log(32, 2))

# print(help(math.log))

# Other import syntax
# import math as mt
# mt.pi

from math import *
print(pi, log(32, 2))


from math import log, pi
# from numpy import asarray

import numpy
print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
     )

# Roll 10 dice
rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)


# Three tools for understanding strange objects

print(type(rolls))

print(dir(rolls))

print(rolls.mean())

print(rolls.tolist())

# help(rolls.ravel)

# help(rolls)

print(rolls + 10)

print(rolls <= 3)

xlist = [[1,2,3],[2,4,6],]
# Create a 2-dimensional array
x = numpy.asarray(xlist)
print("xlist = {}\nx =\n{}".format(xlist, x))

# Get the last element of the second row of our numpy array
print(x[1,-1])

import tensorflow as tf
# Create two constants, each with value 1
a = tf.constant(1)
b = tf.constant(1)
# Add them together to get...
print(a + b)

