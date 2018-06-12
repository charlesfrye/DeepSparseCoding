import os
import numpy as np

params = {
  "model_type": "conv_gdn_autoencoder",
  "model_name": "conv_gdn_autoencoder",
  "version": "0.0",
  "vectorize_data": False,
  "norm_data": False,
  "center_data": False,
  "standardize_data": False,
  "contrast_normalize": False,
  "whiten_data": False,
  "lpf_data": True,
  "lpf_cutoff": 0.7,
  "extract_patches": False,
  "num_colors": 1,
  "downsample_images": True,
  "downsample_method": "resize",
  "num_preproc_threads": 8,
  "im_size_y": 256,
  "im_size_x": 256,
  "batch_size": 25,
  "n_mem": 32768,
  "mem_v_min": -1.0,
  "mem_v_max": 1.0,
  "sigmoid_beta": 1.0,
  "mle_step_size": 0.01,
  "num_mle_steps": 15,
  "num_triangles": 20,
  "input_channels": [1, 128, 128],
  "output_channels": [128, 128, 128],
  "patch_size_y": [9, 5, 5],
  "patch_size_x": [9, 5, 5],
  "strides": [4, 2, 2],
  "memristor_type": "rram",
  "memristor_data_loc": os.path.expanduser("~")+"/CAE_Project/CAEs/data/Partial_Reset_PCM.pkl",
  "optimizer": "adam",#"annealed_sgd",
  "cp_int": 50000,
  "max_cp_to_keep": 1,
  "cp_load": False,
  "log_int": 100,
  "log_to_file": False,
  "gen_plot_int": 1000,
  "save_plots": True,
  "eps": 1e-12,
  "device": "/gpu:0",
  "rand_seed": 1234567890,
  "out_dir": os.path.expanduser("~")+"/Work/Projects/",
  "data_dir": os.path.expanduser("~")+"/Work/Datasets/",
  "data_file":"/media/tbell/datasets/natural_images.txt"}

train_list = ["w"+str(idx) for idx in range(2*len(params["input_channels"]))]
train_list += ["b"+str(idx) for idx in range(2*len(params["input_channels"]))]
train_list += ["w_gdn"+str(idx) for idx in range(len(params["input_channels"]))]
train_list += ["b_gdn"+str(idx) for idx in range(len(params["input_channels"]))]
train_list += ["w_igdn"+str(idx)
  for idx in range(len(params["input_channels"]), 2*len(params["input_channels"]))]
train_list += ["b_igdn"+str(idx)
  for idx in range(len(params["input_channels"]), 2*len(params["input_channels"]))]

#num_batches = (params["num_epochs"]*params["batch_size"])/params["epoch_size"]
weight_lr = [5.0e-4 for _ in range(len(train_list))]
#decay_steps = [int(0.8*num_batches) for _ in range(len(train_list))]
decay_rate = [0.9 for _ in range(len(train_list))]
staircase = [True for _ in range(len(train_list))]

schedule = [
  {"weights": train_list,
  "ent_mult": 0.2,
  "ramp_slope": 1.0,
  "decay_mult": 0.0,
  "noise_var_mult": 0.0,
  "triangle_centers": np.linspace(-1.0, 1.0, params["num_triangles"]),
  "weight_lr": weight_lr,
  "num_epochs": 10,
  #"decay_steps": decay_steps,
  "decay_rate": decay_rate,
  "staircase": staircase}]
