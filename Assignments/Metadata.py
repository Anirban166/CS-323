# importing required libraries:
import numpy as np
import tensorflow.compat.v1 as tf
"""
Creating a 2D tensor which is the result of a matrix multiplication
(performed by tf.matmul()) between a hardcoded 2D tensor and a
tensor formed from random values (using tf.random_uniform)
with a uniform distribution:
"""
y = tf.matmul([[37.0, -23.0], [1.0, 4.0]], tf.random_uniform([2, 2]))

# creating a session and initializing variables within:
with tf.Session() as sess:
  # defining options for the 'sess.run()' call:
  options = tf.RunOptions()
  # enabling our session to output the subgraphs 
  # of our computed graph:
  options.output_partition_graphs = True
  # run with full tracing, i.e. both software and hardware tracing:
  options.trace_level = tf.RunOptions.FULL_TRACE
  # storing and displaying metadata computed over a run/session:
  # creating a container to hold the returned metadata 
  # from tf.RunMetadata():
  metadata = tf.RunMetadata()
  # running a session on our 2D tensor with our specified options
  # and metadata (as initialized above):
  sess.run(y, options=options, run_metadata=metadata)
  # printing the subgraphs that executed on each device:
  print(metadata.partition_graphs)
  # printing the timings of each executed operation,
  # with nanosecond time-precision:
  print(metadata.step_stats)
