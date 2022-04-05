'''
simpler libnet
'''
###################################### Imports

import os
import sys
import numpy as np

from py_extract_class import py_extract as pe
from func import *

###################################### Class

class mapnet:
    def __init__(self,target):
        
        self.target = target
        self.launch()
    
    def launch(self):
        self.find_modules()
        self.find_connections()
        
    def expand(self,root):
        
        self.files = []
        self.expand_recursive(root)
        
    def expand_recursive(self,root):
        
        root_dir = os.listdir(root)

        for i in range(len(root_dir)):
            
            rdi = root_dir[i]
            pthi = root + "/" + rdi
            
            try:
                self.expand_recursive(pthi)
            except:
                self.files.append(pthi)
        
    def find_modules(self):
        
        self.modules = []
        self.expand(self.target)
        
        for x in self.files:
            if x.split(".")[1] == "py":
                self.modules.append(x)
            else:
                pass

    def find_connections(self):
        self.connections = []    
        
        for module in self.modules:
            self.connections.extend(pe(module).connections)