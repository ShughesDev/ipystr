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
        
        self.connections_raw = []    
        
        for module in self.modules:
            self.connections_raw.extend(pe(module).connections)
        
        
        self.connections = []
        
        for connection in self.connections_raw:
            
            raw_dest = connection[0]
            
            raw_source = connection[1]
            raw_source_proc = slash(raw_source.split(".")) + ".py"
            
            found_file = 0
            
            for i in range(len(raw_dest)-1):
                dest_path = slash(raw_dest.split("/"),i+1)
                try:
                    test_dest_path = dest_path + "/" + raw_source_proc
                    
                    test_openfile = open(dest_path + "/" + raw_source_proc,"r")
                    
                    test_openfile.close()
                    
                    found_file = 1
                    
                    output = test_dest_path
                
                except:
                    null = 0
                    
            self.connections.append([connection[0],output,connection[2]])
            
'''    
alpha = mapnet("library_ex")

printm(alpha.connections_raw)
print("---")
printm(alpha.connections)

'''