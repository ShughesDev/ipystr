'''
math_func

'''

import numpy as np


def match_alg(a,b):
    
    la = len(a)
    lb = len(b)
    
    mil = min([la,lb])
    mal = max([la,lb])
    
    n = la + lb - 1
    
    scores = []
    
    for i in range(n):
        
        if i < mil - 1:
            #lower edge
            env = i + 1
            
        
        elif i > n - nil:
            #upper edge
            pass
            
        else:
            env = mil
            
            
def find_pairs(a,b):
    
    pairs = [[],[]]
    
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                pairs[0].append(i)
                pairs[1].append(j)
            else:
                null = 0
                
    return pairs

def eq_ar(a,b):
    
    ret = True
    
    if len(a) != len(b):
        ret = False
    else:
        for i in range(len(a)):
            if a[i] != b[i]:
                ret = False
            else:
                null = 0
    
    return ret
        
        

def find_subsequences(a,b):
        
    la = len(a)
    lb = len(b)
    
    mil = min([la,lb])
    mal = max([la,lb])
    
    scores = []
    
    window_len = 2
    max_window_len = 2
    
    score_index = 0
    
    while window_len <= mil:
        scores.append([])
        for i in range(len(a)-window_len+1):
            for j in range(len(b)-window_len+1):
                
                window_a = a[slice(i,i+window_len)]
                window_b = b[slice(j,j+window_len)]
                
                if eq_ar(window_a,window_b):
                    scores[score_index].append([[i,j],window_len])
                    max_window_len = window_len
                else:
                    null = 0
        
        score_index += 1
        window_len += 1
    
    return(scores[max_window_len-2])

def isin(x,array):
    
    ret = False
    
    for i in array:
        if i == x:
            ret = True
        else:
            null = 0
            
    return ret
        