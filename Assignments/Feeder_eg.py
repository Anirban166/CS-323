# importing required libraries:
import numpy as np
import tensorflow.compat.v1 as tf
# disabling active eager execution:
tf.compat.v1.disable_eager_execution()

# creating a placeholder x that expects a vector of three floating-point 
# values, with a computation that depends on it:
x = tf.placeholder(tf.float32, shape=[3])
# using tf.math.square() to assign the square of x to a variable:
y = tf.square(x)
# note that in the above line, the argument's (x) data type is not specified,
# but it is inferred from the value - i.e. x being a square of a float32 or
# a 32-bit floating point, will remain a float32.
 
# creating a session and initializing our variables: 
with tf.Session() as sess:
  # Feeding a value changes the result that is returned when we evaluate `y`:
  print(sess.run(y, {x: [1.0, 2.0, 3.0]}))  # => "[1.0, 4.0, 9.0]" (squared)
  print(sess.run(y, {x: [0.0, 0.0, 5.0]}))  # => "[0.0, 0.0, 25.0]" (squared)
"""
Now, if we write:
sess.run(y)
It will raise a `tf.errors.InvalidArgumentError`, because we must feed a value 
for a `tf.placeholder()` when evaluating a tensor that depends on it.
--------------------------------------------------------------------------------
Again, if we were to write:
sess.run(y, {x: 37.0})
It will raise `ValueError`, because the shape of `37.0` does not match the 
shape of our placeholder `x`.
"""
