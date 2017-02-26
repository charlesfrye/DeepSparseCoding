"""
Get function that returns the corresponding dataset
Inputs:
  dataset_type: [str] containing the name of the dataset to return
    Current allowed values are: vanHateren, mnist, laplacian
  params: [dict] containing params returned from params/param_picker.py
Outputs:
  dataset: [dataset] object containing the dataset
"""
def get_data(dataset_type, params):
  if dataset_type.lower() == "vanhateren":
    from data.vanHateren import load_vanHateren
    dataset = load_vanHateren(params)
  if dataset_type.lower() == "mnist":
    from data.mnist import load_MNIST
    dataset = load_MNIST(params)
  if dataset_type.lower() == "synthetic":
    assert "num_examples" in params.keys(), (
      "Params must include 'num_examples'")
    from data.synthetic import load_synthetic
    dataset = load_synthetic(params)
  return dataset
