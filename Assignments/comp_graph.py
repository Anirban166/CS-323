import numpy as np
import tensorflow as tf

# A simple computational graph 

a = tf.constant(3.0, dtype=tf.float32)
b = tf.constant(4.0) # also tf.float32 implicitly
total = a + b
print(a)
print(b)
print(total)

# The following code creates a tf.Session object and then invokes its run method to evaluate the total tensor we created
sess = tf.Session()
print(sess.run(total))

#You can pass multiple tensors to tf.Session.run. The run method transparently handles any combination of tuples or dictionaries, as in the following example:
print(sess.run({'ab':(a, b), 'total':total}))

#During a call to tf.Session.run any tf.Tensor only has a single value. 
#For example, the following code calls tf.random_uniform to produce a tf.Tensor that generates a random 3-element vector (with values in [0,1)):

vec = tf.random_uniform(shape=(3,))
out1 = vec + 1
out2 = vec + 2
print(sess.run(vec))
print(sess.run(vec))
print(sess.run((out1, out2)))
