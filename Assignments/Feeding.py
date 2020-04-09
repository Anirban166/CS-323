import numpy as np
import tensorflow as tf

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
z = x + y

We can evaluate this graph with multiple inputs by using the feed_dict argument of the run method to feed concrete values to the placeholder. feed_dict argument can be used to overwrite any tensor in the graph.
sess = tf.Session()
print(sess.run(z, feed_dict={x: 3, y: 4.5}))
print(sess.run(z, feed_dict={x: [1, 3], y: [2, 4]}))
