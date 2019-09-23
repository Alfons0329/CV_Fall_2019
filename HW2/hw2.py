#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import math, sys
import matplotlib.pyplot as plt

'''
savefig sould be done before show
see: https://blog.csdn.net/u010099080/article/details/52912439
'''

sys.setrecursionlimit(100000000)

####### hist part ########
def img_hist(img_in):
    hist = []
    for i in range(256):
        hist.append(0)

    row, col= img_in.shape
    for i in range(0, row):
        for j in range(0, col):
            hist[img_in[i, j]] += 1

    plt.bar(range(0, 256), hist)
    plt.savefig('histogram.png')
    plt.show()
    return 0

####### binarize part ######
def img_binarize(img_in):
    return (img_in > 0x7f) * 0xff

########## IO ##############
img = cv2.imread('lena.bmp', 0)
img_binarized = img_binarize(img)
plt.imshow(img_binarized, cmap = 'gray')
plt.savefig('lena_binarized.png', cmap = 'gray')
#plt.show()

######### CC part ##########
cc_img = (img_binarized == 0xff) * 1
def dfs(i, j, label, row, col):
    if cc_img[i, j] > 1:
        print(i, j, cc_img[i, j])
    if cc_img[i, j] == 1: # only label this kind
        cc_img[i, j] = label
        if i > 0: dfs(i - 1, j, label, row, col)
        if i < row - 1: dfs(i + 1, j, label, row, col)
        if j > 0: dfs(i, j - 1, label, row, col)
        if j < col - 1: dfs(i, j + 1, label, row, col)

    return 0

def connected_components():
    plt.imshow(cc_img, cmap = 'gray')
    row, col = cc_img.shape

    label = 2
    for i in range(0, row):
        for j in range(0, col):
            if cc_img[i, j] == 1: # unlabelled
                dfs(i, j, label, row, col)
                label += 1

    mymap = []
    for i in range(0, row * col):
        mymap.append(0)

    for i in range(0, row):
        for j in range(0, col):
            mymap[cc_img[i, j]] += 1

    #print(mymap)
    return 0

connected_components()
print('finished all image processing')

