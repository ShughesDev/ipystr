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

###################################### Function

def ipystr(target,outname):

    alpha = mn(target)
    
    
    beta = pyyed.Graph()
    
    
    folders = alpha.folders
    
    group_objects = []
    for i in range(len(alpha.folders)):
        group_objects.append([])
        for j in range(len(alpha.folders[i])):
            group_objects[i].append(alpha.folders[i][j]+"_go")
            
    printm(group_objects)
    
    #build groups
    
    for i in range(len(group_objects)):
        for j in range(len(group_objects[i])):
            
            grab_folder = folders[i][j]
            
            if len(grab_folder.split("/")) == 1:
                
                group_objects[i][j]  = beta.add_group(grab_folder)
               
            else:
                
                master = slash(grab_folder.split("/"),1) #string
                
                level_master = len(master.split("/"))-1 #string
                
                print("master:",master,level_master)
                
                for k in range(len(folders[level_master])):
                    if folders[level_master][k] == master:
                        j_val = k
                    else:
                        null = 0
                        
                group_objects[i][j] = group_objects[level_master][j_val].add_group(grab_folder)
                
    #add nodes
    
    module_objects = []
    
    for i in range(len(alpha.modules)):
        
        module = alpha.modules[i]
        
        module_objects.append(module+"_object")
        
    for i in range(len(alpha.modules)):
        
        module = alpha.modules[i]
        
        mod_loc = slash(module.split("/"),1)
        
        for i in range(len(folders)):
            for j in range(len(folders[i])):
                if mod_loc == folders[i][j]:
                    i_val = i
                    j_val = j
                else:
                    null = 0
        
        module_objects[i] = group_objects[i_val][j_val].add_node(module)
        
        
    for connection in alpha.connections:
        source = connection[0]
        dest = connection[1]
        beta.add_edge(source,dest)    
    
    beta.write_graph(outname+".graphml")     
    
