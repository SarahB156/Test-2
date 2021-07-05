# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 13:29:36 2021

@author: sarah
"""

import numpy as np
import h5py
arr = np.random.randn(1000)
print(arr)
with h5py.File('test.hdf5', 'w') as f:
    dset = f.create_dataset("default", data = arr)
with h5py.File('test.hdf5', 'r') as f:
    data = f['default']
print(min(data))