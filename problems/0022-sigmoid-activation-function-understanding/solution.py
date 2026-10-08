import torch

def sigmoid(z: float) -> float:
    """
    Compute the sigmoid activation function.
    Input:
      - z: float or torch scalar tensor
    Returns:
      - sigmoid(z) as Python float rounded to 4 decimals.
    """
    exp_z=torch.exp(torch.tensor(-z))
    sigmoid_value=1/(1+exp_z)

    return round(sigmoid_value.item(),4)
