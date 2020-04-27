# import required libraries:
import numpy as np
import tensorflow as tf
"""
Tensorflow is an open-source library (primarily written in C++)
which is extensively used for building and training ML models.

Tensors are n-dimensional arrays of the base datatypes used in a language.
 
There are different types of tensors such as tf.Variable, tf.constant, 
tf.placeholder and tf.SparseTensor.

A tf.tensor must have a data type and a shape.

For example, lets consider a tf.constant. Its syntax is as follows:
tf.constant(value, dtype, shape, name)

creating a constant tensor with a value of 3 and a data type of float32:
"""
a = tf.constant(3.0, dtype=tf.float32)
# printing the same:
print(a)

# Now lets consider a tf.Variable.
# creating a tf.Variable with value(s) of (3.14159, 2.71828) of the same type:
cool_numbers = tf.Variable([3.14159, 2.71828], tf.float32)
# printing the same:
print(cool_numbers)
