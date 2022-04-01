'''
library network calculator

'''

import os
import sys
import numpy as np

def printm(x):
    for i in range(len(x)):
        print(x[i])

class folder_method:
    def process(self):

        for i in range(len(self.contents)):
            name_i = self.contents[i]
            path = self.root
            
            try:
                a_test = folder(name_i,path)
                type_i = "folder"
            except:
                if self.contents[i].split(".")[1] == "py":
                    type_i = "pyfile"
                else:
                    type_i = "miscfile"
            
            if type_i == "folder":
                self.objects.append("folder" + str(i))
                self.objects[i] = folder(name_i,self.root)
                self.objects[i].launch(self.subfolders)
            
            elif type_i == "pyfile":
                self.objects.append("pyfile" + str(i))
                self.objects[i] = py_file(name_i,self.root)
                self.objects[i].launch(self.subfolders)
                
            elif type_i == "miscfile":
                self.objects.append("miscfile" + str(i))
                self.objects[i] = misc_file(name_i,self.root)
                self.objects[i].launch(self.subfolders)

class basic:
    def __get__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    def launch(self,master_subfolder):
        master_subfolder.append(self.name)
        pass

class folder(basic,folder_method):
    def __init__(self,name,directory):
        self.name = name
        self.direc = directory
        self.type = "folder"
        
        self.root = self.direc + "/" + self.name
        #print("root:",self.root)
        self.contents = os.listdir(self.root)
        
    def launch(self,master_subfolder):
        #master_subfolder.append([])
        #print("folder")
        
        self.objects = []
        self.subfolders = []
        
        #self.makeup = np.array([0,0,0],dtype="int") #[folders,pyfiles,miscfiles]
        self.process()
        
        master_subfolder.append(self.subfolders)

class py_file(basic):
    def __init__(self,name,directory):
        self.name = name
        self.directory = directory
        self.type = "pyfile"

class misc_file(basic):
    def __init__(self,name,directory):
        self.name = name
        self.directory = directory
        self.type = "miscfile"
        
class process(folder_method):
    def __init__(self,root):

        self.root = root
        self.contents = os.listdir(self.root)
        
        self.objects = []
        self.subfolders = []
        
        #self.makeup = np.array([0,0,0],dtype="int") #[folders,pyfiles,miscfiles]
        self.process()  

target = "sample"
alpha = process(target)

printm(alpha.subfolders)
print("-----")
print(alpha.objects[1].objects)