'''
simpler libnet
'''
###################################### Imports

import os
import sys
import numpy as np

###################################### Misc Functions

def printm(x):
    for i in x:
        print(i)
        
def printmi(x):
    for i in range(len(x)):
        print(i,",",x[i])
        
        
###################################### Find Module Names

def process(root,arr):
        
    root_dir = os.listdir(root)

    for i in range(len(root_dir)):
        
        rdi = root_dir[i]
        pthi = root + "/" + rdi
        
        try:
            process(pthi,arr)
        except:
            arr.append(pthi)

target = "sample"

array = []
alpha = process(target,array)
#printm(array)

proc_array = []
for x in array:
    if x.split(".")[1] == "py":
        proc_array.append(x)
    else:
        pass
    
modules = proc_array
#printmi(modules)
###################################### Read Modules to find Import Connections


    
