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

target = "library_ex"

alpha = mn(target)




'''
printmi(alpha.modules)
print("---")
printmi(alpha.connections)


'''
#printmi(alpha.unchecked_connections)



beta = pyyed.Graph()

for module in alpha.modules:
    beta.add_node(module)
    
for connection in alpha.connections:
    source = connection[0]
    dest = connection[1]
    beta.add_edge(source,dest)
    
beta.write_graph(target+".graphml")