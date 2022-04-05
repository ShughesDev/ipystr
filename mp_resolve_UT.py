'''
module path resolver UT
'''
#################### Imports

import pytest

from mp_resolve import modulepath

#################### Tests

def test_modulepath():
    
    path = "folder1/folder1a/script_a.py"
    module = "script_b"
    
    actual = modulepath(path,module)
    
    expected_path = "folder1/folder1a/script_a"
    expected_module = "folder1/folder1a/script_b"

    assert actual.path == expected_path
    assert actual.module == expected_module
    
test_modulepath()