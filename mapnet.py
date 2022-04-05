'''
simpler libnet
'''
###################################### Imports

import os
import sys
import numpy as np

from py_extract_class import py_extract as pe
from func import *
from math_func import *

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
        
        unchecked_connections = []    
        
        for module in self.modules:
            unchecked_connections.extend(pe(module).connections)
        
        self.unchecked_connections = unchecked_connections
        
        self.connections = []
        #check module is in same location as import dest
        for uc in unchecked_connections:
            path_loc_splt = uc[0].split(".")[0].split("/")
            mod_spl = uc[1].split(".")
            
            path = ""
            for i in range(len(path_loc_splt)-1):
                path += path_loc_splt[i]
                if i != len(path_loc_splt)-2:
                    path += "/"
                else:
                    null = 0
                    
            check = uc[1].split(".")[0]
            
            if isin(check,os.listdir(path)):
                #folder IS case
                c0 = uc[0].split(".")[0]
                c1 = path
                
                for i in range(len(mod_spl)):
                    c1 += "/"
                    c1 += mod_spl[i]
                
                self.connections.append([c0,c1,uc[2]])
                
            elif isin(check+".py",os.listdir(path)):
                #.py file IS case
                c0 = uc[0].split(".")[0]
                c1 = path
                
                for i in range(len(mod_spl)):
                    c1 += "/"
                    c1 += mod_spl[i]
                
                self.connections.append([c0,c1,uc[2]])
                
            else:
                # isn't case
                null = 0