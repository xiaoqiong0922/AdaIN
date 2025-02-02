# -*- coding: utf-8 -*-


from torch.utils.data import sampler
import numpy as np

def InfiniteSampler(n):
    i = n - 1
    order = np.random.permutation(n)  # disrupt range(n)
    
    while True:
        yield order[i]
        i += 1
        if i >= n:
            np.random.seed()
            order = np.random.permutation(n)
            i = 0
    

class InfiniteSamplerWrapper(sampler.Sampler):
    def __init__(self, data_source):
        self.num_samples = len(data_source)

    def __iter__(self):
        return iter(InfiniteSampler(self.num_samples))
    
    def __len__(self):
        return 2 ** 31
























