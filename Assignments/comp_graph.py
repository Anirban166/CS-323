# TensorFlow programs work by first building a graph of tf.Tensor objects, 
# detailing how each tensor is computed based on the other available tensors 
# and then by running parts of the graph to achieve desired results.

# import required libraries:
import numpy as np
import tensorflow.compat.v1 as tf # going with tensorflow v1.x

# creating a constant with a value of 3 and a data type of float32:
a = tf.constant(3.0, dtype=tf.float32)
"""
If data type is not explicitly specified, then its implicitly drawn
from the type of value given (1 -> int32; 1.0 -> float32)

For example, b gets assigned a data type of float32 implicitly from 4.0:
"""
b = tf.constant(4.0) 
# add constant tensors a and b, storing result in a variable:
total = a + b
# print all of them: (the two individual constants and their sum respectively)
print(a)
print(b)
print(total)

# creating a tf.Session object and invoking its run method to evaluate 
# the 'total' tensor that we created above: 
sess = tf.Session()
# printing the same:
print(sess.run(total))

"""
We can pass multiple tensors to tf.Session.run. The run method accepts
and manages any combination of tuples or dictionaries, 
as can be seen in the following example:
"""
print(sess.run({'ab':(a, b), 'total':total}))

"""
During a call to tf.Session.run, any tf.Tensor only has a single value. 
For example, the following code calls tf.random_uniform to produce a tf.Tensor 
that generates a random 3-element vector (with values in [0,1)):
"""
# creating a random 3-element vector:
vec = tf.random_uniform(shape=(3,))
# adding 1 and 2 to the 3-values respectively: (random at each vec instance)
out1 = vec + 1
out2 = vec + 2
# printing the the values, with singular values each: (notice no commas)
print(sess.run(vec))
print(sess.run(vec))
# printing the 3-element arrays:
print(sess.run((out1, out2)))
