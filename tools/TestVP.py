import numpy as np
import torch
from vp_suite import VPSuite

from sys import platform

#print(VPSuite().list_available_models())
#print("-----------------------------------------")
#print(VPSuite().list_available_datasets())

A = torch.arange(4 * 10 * 4 * 4).reshape(4,10,4,4)


C = A[:,[True,False,True,False,False,False,True,True,False,False]]
print(C.shape)
print(C)