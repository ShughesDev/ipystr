'''
misc functions
'''

###################################### Imports

import os
import sys
import numpy as np

###################################### Functions

def printm(x):
    for i in x:
        print(i)
        
def printmi(x):
    for i in range(len(x)):
        print(i,",",x[i])
        
def slash(ar,offset = 0):
    ret = ""
    for i in range(len(ar) - offset):
        ret += ar[i]
        if i != len(ar) - 1 - offset:
            ret += "/"
        else:
            null = 0
            
    return ret
        
        