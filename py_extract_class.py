'''
python script import extractor
'''

class py_extract:
    
    def __init__(self,path = None):
        self.path = path
        try:
            self.routine()
            
        except:
            print("Initialised pyextract with no path.")
    
    def routine(self):
        self.extract()
        self.filter_imports()
        
    
    def extract(self):
        self.code = []
        for line in open(self.path,"r"):
            self.code.append(line)
            
        #print(self.code)
    
    def filter_imports(self):
        
        self.import_lines = []
        
        for line in self.code:
            if len(line.split("import")) > 1:
                self.import_lines.append(line.split("\n")[0])
    
    def filter_frm_std(self):
        
        self.frm = []
        self.std = []
        
        for line in self.import_lines:
            
            if len(line.split("from"))>1:
                self.frm.append(line)
            else:
                self.std.append(line)
        
'''
path = "sample/library_ex/script_b.py"

alpha = py_extract(path)
'''

'''
sample = modules[3]
print(sample)

sample_code = []
for line in open(sample,"r"):
    sample_code.append(line)
    
#printm(sample_code)

imports = []
for line in sample_code:
    if len(line.split("import")) > 1:
        imports.append(line.split("\n")[0])
        
    else:
        pass
print("----")
print(imports)
print("----")
std_imp = []
frm_imp = []

for line in imports:
    if len(line.split("from"))>1:
        frm_imp.append(line)
    else:
        std_imp.append(line)
    
print("---")
print(frm_imp)
print("---")
print(std_imp)
print("---")

#### frm imps

for i in range(len(frm_imp)):
    
'''