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
        self.find_folders()
        
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
            
    def find_folders(self):
        
        folders_unsorted = []
        
        for module in self.modules:
            
            module_path = module.split("/")
            
            for i in range(len(module_path)-1):
                
                grab = slash(module_path,(1+i))
                
                if isin(grab,folders_unsorted) == False:
                    folders_unsorted.append(grab)
                else:
                    null = 0 
        
        depth = 0
        
        for folder in folders_unsorted:
            if len(folder.split("/")) > depth:
                depth = len(folder.split("/"))
        
        
        
        self.folders = np.zeros((depth),dtype='object')
        
        #print(self.folders)
        #print(len(self.folders))
        for i in range(len(self.folders)):
            self.folders[i] = []
        
        for folder in folders_unsorted:
            folder_depth = len(folder.split("/"))
            
            self.folders[folder_depth-1].append(folder)
        

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