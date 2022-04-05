'''
module path resolver
'''
#################### Imports
import numpy as np
from math_func import *

#################### Class
class modulepath:
    def __init__(self,path,module):
        self.path_raw = path
        self.module_raw = module
        
        self.launch()
        
    def launch(self):
        self.convert_path()
        self.convert_module()
    
    def convert_path(self):
        
        self.path = self.path_raw.split(".")[0]
        
    def convert_module(self):
        
        ar_path = self.path.split("/")
        ar_mod = self.module_raw.split(".")
        
        self.module = ""
        
        for i in range(len(ar_path)-1):
            self.module += ar_path[i]
            self.module += "/"
        
        for i in range(len(ar_mod)):
            self.module += ar_mod[i]
            
            if i != (len(ar_mod) - 1):
                self.module += "/"
            else:
                null = 0
        
            
        