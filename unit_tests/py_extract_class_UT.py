'''
python script import extractor
UT
'''

#################### Imports

import pytest

from py_extract_class import py_extract

#################### Tests

def test_py_extract_filter_imports():
    
    alpha = py_extract()
    
    code_sample = ["import matplotlib.pyplot as plt\n",
                   "from a import b\n",
                   "\n",
                   "print('test')"]
    
    alpha.code = code_sample
    
    alpha.filter_imports()
    
    actual = alpha.import_lines
    
    expected = ["import matplotlib.pyplot as plt",
                "from a import b"]
    
    print(actual)
    
    for i in range(len(actual)):
        assert actual[i] == expected[i]
        
def test_py_extract_filter_frm_std():
    
    alpha = py_extract()
    
    import_lines = ["import matplotlib.pyplot as plt",
                "from a import b"]
    
    alpha.import_lines = import_lines
    
    expected_std = ["import matplotlib.pyplot as plt"]
    expected_frm = ["from a import b"]
    
    alpha.filter_frm_std()
    
    actual_std = alpha.std
    actual_frm = alpha.frm
    
    for i in range(len(actual_std)):
        assert actual_std[i] == expected_std[i]
        
    for i in range(len(actual_frm)):
        assert actual_frm[i] == expected_frm[i]
        
def test_py_extract_filter_frm():
    
    alpha = py_extract()
    
    alpha.path = "test_source"
    alpha.frm = ["from a import b",
                "from b import c, d",
                "from d import a as b"]
    
    expected = [["test_source","a","b"],
                ["test_source","b","c"],
                ["test_source","b","d"],
                ["test_source","d","a"]]
    
    alpha.filter_frm()
    
    actual = alpha.connections
    
    for i in range(len(actual)):
        for j in range(len(actual[i])):
            assert actual[i][j] == expected[i][j]
            #print(actual[i][j],",",expected[i][j],"\n-------\n")
        #print(actual[i],"\n",expected[i],"\n-------\n")
    
def test_py_extract_filter_std():
    
    alpha = py_extract()
    
    alpha.path = "test_source"
    alpha.std = ["import a",
                "import a, b",
                "import a as b"]
    
    expected = [["test_source","a","*"],
                ["test_source","a","*"],
                ["test_source","b","*"],
                ["test_source","a","*"]]
    
    alpha.filter_std()
    
    actual = alpha.connections
    
    for i in range(len(actual)):
        for j in range(len(actual[i])):
            assert actual[i][j] == expected[i][j]
            #print(actual[i][j],",",expected[i][j],"\n-------\n")
        #print(actual[i],"\n",expected[i],"\n-------\n")