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
from ipystr import ipystr
from math_func import *

###################################### Program

target = "library_ex"

ipystr(target,"runtests/test_all")