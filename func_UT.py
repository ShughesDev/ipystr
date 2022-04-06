'''
misc functions UT
'''

###################################### Imports

import os
import sys
import numpy as np

from func import *

###################################### Tests

def test_slash():
    
    actual = slash(["a","b","c"])
    
    expected = "a/b/c"
    
    assert actual == expected
    
def test_slash2():
    
    actual = slash(["a","b","c"],1)
    
    expected = "a/b"
    
    assert actual == expected