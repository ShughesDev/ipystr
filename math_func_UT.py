'''
math_func_UT

'''

from math_func import *

import pytest

#######

def test_match_alg():
    
    a = [1,5,4,2,3,4]
    b = [4,2,3,4,5,7]
    
    expected = [[2,3,4,5],[0,1,2,3]]
    
    actual = match_alg(a,b)
    
    for i in range(len(expected)):
        for j in range(len(expected[i])):
            assert expected[i][j] == actual[i][j]
            
            
def test_find_pairs():
    
    a = [0,3,2]
    b = [0,1,6]
    
    expected = [[0],[0]]
    actual = find_pairs(a,b)
    
    for i in range(len(expected)):
        for j in range(len(expected[i])):
            assert expected[i][j] == actual[i][j]
            
            
def test_find_subsequences():
    
    a = [0,1,5,3,2,3]
    b = [1,5,3,2,6,3]
    
    actual = find_subsequences(a,b)
    
    #print(actual)
    
    #expected = [[[1,0],4]]
    assert actual[0][0][0] == 1
    assert actual[0][0][1] == 0
    assert actual[0][1] == 4
    
def test_find_subsequences_nonecase():
    
    a = ["a","b","c"]
    b = ["d","e"]
    
    actual = find_subsequences(a, b)
    
    assert actual == []

def test_eq_ar():
    a = [0,1,2]
    b = [0,1,2]
    
    actual = eq_ar(a,b)
    
    assert actual
    
def test_isin():
    
    assert isin(1,[1,2,3])