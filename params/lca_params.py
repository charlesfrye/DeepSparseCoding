import os
params = {
  "model_type": "lca",
  "model_name": "lca",
  "version": "0.0",
  "num_images": 150,
  "vectorize_data": True,
  "norm_data": False,
  "center_data": True,#False,
  "standardize_data": False,
  "contrast_normalize": False,
  "whiten_data": True,
  "whiten_method": "FT",
  "lpf_data": False, # only for ZCA
  "lpf_cutoff": 0.7,
  "extract_patches": True,
  "num_patches": 1e6,
  "patch_edge_size": 16,
  "overlapping_patches": True,
  "randomize_patches": True,
  "patch_variance_threshold": 0.0,
  "batch_size": 100,
  "num_neurons": 768,
  "num_steps": 50,
  "dt": 0.001,
  "tau": 0.03,
  "rectify_a": True,
  "norm_weights": True,
  "thresh_type": "soft",
  "optimizer": "annealed_sgd",
  "cp_int": 10000,
  "max_cp_to_keep": 1,
  "cp_load": False,
  "cp_load_name": "pretrain",
  "cp_load_step": None, # latest checkpoint
  "cp_load_ver": "0.0",
  "cp_load_var": ["phi"],
  "log_int": 100,
  "log_to_file": True,
  "gen_plot_int": 1000,
  "save_plots": True,
  "eps": 1e-9,
  "device": "/gpu:0",
  "rand_seed": 123456789,
  "out_dir": os.path.expanduser("~")+"/Work/Projects/",
  "data_dir": os.path.expanduser("~")+"/Work/Datasets/"}

schedule = [
  {"weights": ["phi"],
  "sparse_mult": 0.8,
  "weight_lr": [0.01],
  "decay_steps": [int(1e5*0.5)],
  "decay_rate": [0.8],
  "staircase": [True],
  "num_batches": int(1e5)}]
