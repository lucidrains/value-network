import torch
from torch.nn import Module

# functions

def exists(v):
    return v is not None

def default(v, d):
    return v if exists(v) else d

# network

class ValueNetwork(Module):
    def __init__(self):
        super().__init__()
