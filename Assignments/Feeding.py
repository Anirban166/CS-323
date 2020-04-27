# importing required libraries:
import numpy as np
import tensorflow.compat.v1 as tf 
"""
We use tf.placeholder variables here, where:

A placeholder is a variable that will be assigned data to at a later date. 
It allows us to create our operations and build our computation graph, 
without the need of data at the moment of creation. 

creating two placeholder tensors of float32 data type and assigning their
sum to a third variable:
"""
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
z = x + y

# We can evaluate this graph with multiple inputs by using the feed_dict
# argument of the run method to feed concrete values to the placeholder. 
# feed_dict argument can be used to overwrite any tensor in the graph.
sess = tf.Session()
print(sess.run(z, feed_dict={x: 3, y: 4.5}))
print(sess.run(z, feed_dict={x: [1, 3], y: [2, 4]}))
