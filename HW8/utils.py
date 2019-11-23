#!/usr/bin/env python
# coding: utf-8
# NTU CSIE, Computer Vision HW8 utils, R08922024, Alfons Hwu
import numpy as np

####### dilation ######
def dilation(a, b):
    ra, ca = a.shape # original image
    res = np.zeros(a.shape, dtype = 'int32')
    
    for ai in range(ra):
        for aj in range(ca):
                
                max_value = 0
                for b_each in b:
                    bi, bj = b_each
                    if  ai + bi >= 0 and ai + bi < ra and aj + bj >= 0 and aj + bj < ca: 
                        # extend the value
                        max_value = max(max_value, a[ai + bi, aj + bj])
                
                res[ai, aj] = max_value 
                        
    return res 

####### erosion #######
def erosion(a, b):
    ra, ca = a.shape # original image
    res = np.zeros(a.shape, dtype = 'int32')
    
    for ai in range(ra):
        for aj in range(ca):
                
                min_value = 0x100
                for b_each in b:
                    bi, bj = b_each
                    if  ai + bi >= 0 and ai + bi < ra                     and aj + bj >= 0 and aj + bj < ca: 
                        # extend the value
                        min_value = min(min_value, a[ai + bi, aj + bj])
                    
                res[ai, aj] = min_value
    
    return res 

####### opening #######
def opening(a, b):
    return dilation(erosion(a, b), b)

####### closing #######
def closing(a, b):
    return erosion(dilation(a, b), b)