'''
python script import extractor
'''

class py_extract:
    '''
    extractor for import lines:
        
        from a import b
        from a import b, c, d
        import a
        import a as b
    
    '''
    def __init__(self,path = None):
        self.path = path
        
        self.connections = [] #[filepath,modulepath,function]
        
        try:
            self.routine()
            
        except:
            print("Initialised pyextract with no path.")
    
    def routine(self):
        self.extract()
        self.filter_imports()
        self.filter_frm_std()
        self.filter_frm()
        self.filter_std()
    
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
    
    def filter_frm(self):
        
        for line in self.frm:
            line_a = line.split("from ")[1]
            line_b = line_a.split(" import ")
            source = line_b[0]
            #print(line_b)
            func = line_b[1].split(" as")[0].split(", ")
            
            for function in func:
                self.connections.append([self.path,source,function])
                
    def filter_std(self):
        
        for line in self.std:
            line_b = line.split("import ")[1]
            source = line_b.split(" as")[0].split(", ")
            
            for module in source:
                self.connections.append([self.path,module,"*"])
    
        

path = "sample"
alpha = py_extract(path)

