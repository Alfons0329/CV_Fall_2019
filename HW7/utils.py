#!/usr/bin/env python
# coding: utf-8
# NTU CSIE, Computer Vision HW7 utils, R08922024, Alfons Hwu

import cv2
import math, sys
import matplotlib.pyplot as plt
import numpy as np

####### IO ############
img = cv2.imread('lena.bmp', cv2.IMREAD_GRAYSCALE)

####### binarize ######
def img_binarize(img_in):
    return (img_in > 0x7f) * 0xff

####### yokoi core ####
def do_yokoi(img_in):
    row, col = img_in.shape

    # yokoi h op
    def h(b, c, d, e):
        if b == c and (d != b or e != b):
            return 'q'
        if b == c and (d == b and e == b):
            return 'r'

        return 's'

    # main part of yokoi connectivity
    res = np.zeros(img_in.shape, np.int)
    for i in range(row):
        for j in range(col):
            if img_down[i, j] > 0:
                if i == 0:
                    # top-left
                    if j == 0:
                        x7, x2, x6 = 0, 0, 0
                        x3, x0, x1 = 0, img_down[i, j], img_down[i, j + 1]
                        x8, x4, x5 = 0, img_down[i + 1, j], img_down[i + 1, j + 1]
                    # top-right
                    elif j == col - 1:
                        x7, x2, x6 = 0, 0, 0
                        x3, x0, x1 = img_down[i, j - 1], img_down[i, j], 0
                        x8, x4, x5 = img_down[i + 1, j - 1], img_down[i + 1, j], 0
                    # top-row
                    else:
                        x7, x2, x6 = 0, 0, 0
                        x3, x0, x1 = img_down[i, j - 1], img_down[i, j], img_down[i, j + 1]
                        x8, x4, x5 = img_down[i + 1, j - 1], img_down[i + 1, j], img_down[i + 1, j + 1]
                elif i == row - 1:
                    # bottom-left
                    if j == 0:
                        x7, x2, x6 = 0, img_down[i - 1, j], img_down[i - 1, j + 1]
                        x3, x0, x1 = 0, img_down[i, j], img_down[i, j + 1]
                        x8, x4, x5 = 0, 0, 0
                    # bottom-right
                    elif j == col - 1:
                        x7, x2, x6 = img_down[i - 1, j - 1], img_down[i - 1, j], 0
                        x3, x0, x1 = img_down[i, j - 1], img_down[i, j], 0
                        x8, x4, x5 = 0, 0, 0
                    # bottom-row
                    else:
                        x7, x2, x6 = img_down[i - 1, j - 1], img_down[i - 1, j], img_down[i - 1, j + 1]
                        x3, x0, x1 = img_down[i, j - 1], img_down[i, j], img_down[i, j + 1]
                        x8, x4, x5 = 0, 0, 0
                else:
                    # leftmost-row
                    if j == 0:
                        x7, x2, x6 = 0, img_down[i - 1, j], img_down[i - 1, j + 1]
                        x3, x0, x1 = 0, img_down[i, j], img_down[i, j + 1]
                        x8, x4, x5 = 0, img_down[i + 1, j], img_down[i + 1, j + 1]
                    # rightmost-column
                    elif j == col - 1:
                        x7, x2, x6 = img_down[i - 1, j - 1], img_down[i - 1, j], 0
                        x3, x0, x1 = img_down[i, j - 1], img_down[i, j], 0
                        x8, x4, x5 = img_down[i + 1, j - 1], img_down[i + 1, j], 0
                    #the rest, inner
                    else:
                        x7, x2, x6 = img_down[i - 1, j - 1], img_down[i - 1, j], img_down[i - 1, j + 1]
                        x3, x0, x1 = img_down[i, j - 1], img_down[i, j], img_down[i, j + 1]
                        x8, x4, x5 = img_down[i + 1, j - 1], img_down[i + 1, j], img_down[i + 1, j + 1]

                a1 = h(x0, x1, x6, x2)
                a2 = h(x0, x2, x7, x3)
                a3 = h(x0, x3, x8, x4)
                a4 = h(x0, x4, x5, x1)

                cnt = 0
                if a1 == 'r' and a2 == 'r' and a3 == 'r' and a4 == 'r':
                    cnt = 5
                else:
                    cnt = 0
                    for a_i in [a1, a2, a3, a4]:
                        if a_i == 'q':
                            cnt += 1
                
                res[i, j] = cnt
                
    return res

####### ib core #######
def do_ib(img_in):

    def h(c, d):
        # interior content
        if c == d:
            return c         
        # border content
        else
            return 'b'

    res = np.zeros(img_in.shape, np.int)
    for i in range(row):
        for j in range(col):
            if img_down[i, j] > 0:
                x1, x2, x3, x4 = 0, 0, 0, 0
                if i == 0:
                    # top-left
                    if j == 0:
                        x1, x4 = img_in[i, j + 1], img_in[i + 1, j]
                    # top-right
                    elif j == col - 1:
                        x3, x4 = img_in[i, j - 1], img_in[i + 1, j]
                    # top-row
                    else:
                        x1, x3, x4 = img_in[i, j + 1], img_in[i, j - 1], img_in[i + 1, j]
                elif i == row - 1:
                    # bottom-left
                    if j == 0:
                        x1, x2 = img_in[i, j + 1], img_in[i - 1, j]
                    # bottom-right
                    elif j == col - 1:
                        x2, x3 = img_in[i - 1, j], img_in[i, j - 1]
                    # bottom-row
                    else:
                        x1, x2, x3 = img_in[i, j + 1], img_in[i - 1, j], img_in[i, j - 1]
                else:
                    # leftmost-row
                    if j == 0:
                        x1, x2, x4 = img_in[i, j + 1], img_in[i - 1, j], img_in[i + 1, j]
                    # rightmost-colmn
                    elif j == col - 1:
                        x2, x3, x4 = img_in[i - 1, j], img_in[i, j - 1], img_in[i + 1, j]
                    # the rest, inner
                    else:
                        x1, x2, x3, x4 = img_in[i, j + 1], img_in[i - 1, j], img_in[i, j - 1], img_in[i + 1, j]

                x1 /= 255
                x2 /= 255
                x3 /= 255
                x4 /= 255
                a1 = h(1, x1)
                a2 = h(a1, x2)
                a3 = h(a2, x3)
                a4 = h(a3, x4)
                if a4 == 'b':
                    res[i, j] = 2
                else:
                    res[i, j] = 1
    
    return res