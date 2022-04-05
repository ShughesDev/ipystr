'''
ipystr
'''
###################################### Imports

import os
import sys
import numpy as np

import pyyed

from func import *
from mapnet import mapnet as mn

###################################### Program

target = "sample"

alpha = mn(target)




'''
printmi(alpha.modules)
print("---")
printmi(alpha.connections)


'''
#printmi(alpha.unchecked_connections)


'''
beta = pyyed.Graph()

for module in alpha.modules:
    beta.add_node(module)
    
'''