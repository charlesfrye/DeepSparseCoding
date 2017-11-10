import os
params = {
  "model_type": "MLP",
  "model_name": "test",
  "version": "0.0",
  "optimizer": "annealed_sgd",
  "vectorize_data": True,
  "rectify_a": True,
  "norm_a": False,
  "norm_weights": True,
  "batch_size": 100,
  "num_classes": 10,
  "num_hidden": 400,
  "num_val": 10000,
  "num_labeled": 50000,
  "cp_int": 2000,
  "max_cp_to_keep": 5,
  "val_on_cp": True,
  "cp_load": False,
  "cp_load_name": "pretrain",
  "cp_load_step": 150000,
  "cp_load_ver": "0.0",
  "cp_load_var": ["w1"],
  "log_int": 1,
  "log_to_file": False,
  "gen_plot_int": 10,
  "save_plots": True,
  "eps": 1e-12,
  "device": "/cpu:0",
  "rand_seed": 1234567890,
  "out_dir": os.path.expanduser("~")+"/Work/Projects/",
  "data_dir": os.path.expanduser("~")+"/Work/Datasets/"}

schedule = [
  {"weights": ["w1", "w2", "bias1", "bias2"],
  "weight_lr": [0.01, 0.001, 0.01, 0.001],
  "decay_steps": [2000]*4,
  "decay_rate": [0.8]*4,
  "staircase": [True]*4,
  "num_batches": 4000}]
