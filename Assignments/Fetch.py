# import required libraries:
import numpy as np
import tensorflow.compat.v1 as tf
# creating a two dimensional constant tensor:
x = tf.constant([[37.0, -23.0], [1.0, 4.0]])
# generating a variable with a random tensor of uniform distribution:
w = tf.Variable(tf.random_uniform([2, 2]))
# taking two matrix tensors and multiplying them using matmul() function:
y = tf.matmul(x, w)
# applying the softmax activation function which turns numbers into 
# probabilities which sum to one: (under neural net or tf.nn operations)
output = tf.nn.softmax(y)
# specfiying init_op as the initializer for w:
init_op = w.initializer
# printing the values:
print("x:",x) 
print("w:",w)
print("y:",y)
print("Output:",output)
print("init_op:",init_op)
"""
To run operations on the variables, we require to create a tensorflow session
or tf.session (it allows us to execute graphs).
"""
with tf.Session() as sess: 
  # computing output of the graph by running initializer: (on w)
  sess.run(init_op)
  # sess.run(output)` returns a NumPy array containing the result of the
  # computation, hence we print it:
  print(sess.run(output))
  # Evaluate `y` and `output` where `y` will be computed once, and its result
  # is used both to return `y_val` and as an input to the `tf.nn.softmax()`
  # op. (Both `y_val` and `output_val` will be NumPy arrays)
  y_val, output_val = sess.run([y, output])
