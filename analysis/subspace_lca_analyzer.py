import os
import numpy as np
import tensorflow as tf
from analysis.lca_analyzer import LCA_Analyzer
import utils.data_processing as dp

class SUBSPACE_LCA_Analyzer(LCA_Analyzer):
  def __init__(self, params):
    super(SUBSPACE_LCA_Analyzer, self).__init__(params)
    self.var_names += ["weights/group_weights:0"]
    self.var_names += ["inference/group_activity:0"]

  def compute_pooled_activations(self, images):
    """
    Computes the 2nd layer output code for a set of images.
    """
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    with tf.Session(config=config, graph=self.model.graph) as sess:
      feed_dict = self.model.get_feed_dict(images)
      sess.run(self.model.init_op, feed_dict)
      self.model.load_weights(sess, self.cp_loc)
      activations = sess.run(self.model.group_activity, feed_dict)
    return activations
