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