import os
params = {
  "model_type": "dsc",
  "model_name": "test",
  "version": "0.0",
  "num_images": 100,
  "vectorize_images": True,
  "norm_images": False,
  "whiten_images": False,
  "contrast_normalize": False,
  "extract_patches": True,
  "num_patches": 1e3,
  "patch_edge_size": 16,
  "overlapping_patches": True,
  "randomize_patches": True,
  "patch_variance_threshold": 1e-6,
  "batch_size": 100,
  "norm_weights": False,
  "optimizer": "annealed_sgd",
  "rectify_u": False,
  "rectify_v": False,
  "num_u": 576,
  "num_v": 20,
  "num_steps": 20,
  "cp_int": 2000,
  "max_cp_to_keep": 2,
  #"w_init_loc": os.path.expanduser("~")+"/Work/Projects/pretrain/analysis/0.0/weights/phi.npz",
  "w_init_loc": None,
  "cp_load": False,
  "cp_load_name": "pretrain",
  "cp_load_step": 120000,
  "cp_load_ver": "0.0",
  "cp_load_var": ["phi"],
  "cp_set_var": ["a"],
  "log_int": 1,
  "log_to_file": False,
  "gen_plot_int": 2,
  "save_plots": True,
  "eps": 1e-12,
  "device": "/cpu:0",
  "rand_seed": 1234567890,
  "out_dir": os.path.expanduser("~")+"/Work/Projects/",
  "data_dir": os.path.expanduser("~")+"/Work/Datasets/"}

schedule = [
  #{"weights": ["a"],
  #"recon_mult": 0.1,
  #"sparse_mult": 0.0,
  #"a_decay_mult": 1.0,
  #"b_decay_mult": 0.0,
  #"u_step_size": 0.01,
  #"v_step_size": 0.0,
  #"weight_lr": [0.1],
  #"decay_steps": [2000],
  #"decay_rate": [0.9],
  #"staircase": [True],
  #"num_batches": 2000}]#,

  {"weights": ["a", "b"],
  "recon_mult": 1.0,
  "sparse_mult": 0.1,
  "a_decay_mult": 0.8,
  "b_decay_mult": 0.8,
  "u_step_size": 0.01,
  "v_step_size": 0.001,
  "weight_lr": [0.1, 0.001],
  "decay_steps": [5000]*2,
  "decay_rate": [0.8]*2,
  "staircase": [True]*2,
  "num_batches": 5000}]
