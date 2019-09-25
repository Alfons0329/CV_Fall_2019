#!/usr/bin/env python
# coding: utf-8

# In[14]:


import cv2
import math, sys
import matplotlib.pyplot as plt
from PIL import Image

'''
savefig sould be done before show
see: https://blog.csdn.net/u010099080/article/details/52912439
'''

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
#plt.imshow(img, cmap = 'gray')
#plt.show()

img_binarized = img_binarize(img)
#plt.imshow(img_binarized, cmap = 'gray')
plt.savefig('lena_binarized.png', cmap = 'gray')
#plt.show()

img_hist(img)

######### CC part ##########
parent_label = []
cc_img = (img_binarized == 0xff) * 1

def union_find(label):
    original_label = label
    cnt = 0
    row, col = cc_img.shape
    while label != parent_label[label] and cnt < row * col:
        label = parent_label[parent_label[label]]
        cnt += 1

    parent_label[original_label] = label # path compression to avoid TLE
    return label

def draw_rect(img, left, right, top, bottom, color):
    return 0

def draw_cent():
    return 0

def connected_components():
    # set parent label
    # plt.imshow(cc_img, cmap = 'gray')
    row, col = cc_img.shape
    for i in range(row * col):
        parent_label.append(i)

    # do connected components
    label = 2
    for i in range(row):
        for j in range(col):
            ok1 = 0
            ok2 = 0
            if cc_img[i, j] == 1:
                if j - 1 >= 0 and cc_img[i, j - 1] > 1: # left has already labeled
                    #print(i, j, 'type 1,', end = '')
                    cc_img[i, j] = union_find(cc_img[i, j - 1])
                    ok1 = 1

                if i - 1 >= 0 and cc_img[i - 1, j] > 1: # up has already labeled
                    #print(i, j, 'type 2,', end = '')
                    if ok1: # set the connected component to make left = up
                        parent_label[cc_img[i, j]] = union_find(cc_img[i - 1, j])
                    else:
                        cc_img[i, j] = union_find(cc_img[i - 1, j])

                    ok2 = 1
                if ok2 == 0 and ok1 == 0:
                    #print(i, j, 'type 3,', end = '')
                    cc_img[i, j] = label
                    label += 1
        #print()

    '''
    for i in range(row):
        print()
        for j in range(col):
            print(cc_img[i, j], end = '')

    for i in range(row):
        print()
        for j in range(col):
            print(cc_img[i, j], end = '')
    '''

    for i in range(row):
        print()
        for j in range(col):
            print('%3d'%(cc_img[i, j]), end = '')

    # union and find merging
    for i in range(row):
        for j in range(col):
            if cc_img[i, j] > 1:
                #print('%d par--> %d,' %(cc_img[i, j], union_find(cc_img[i, j])), end = '')
                cc_img[i, j] = union_find(cc_img[i, j])

    mymap = []
    for i in range(0, row * col):
        mymap.append(0)

    for i in range(0, row):
        for j in range(0, col):
            mymap[cc_img[i, j]] += 1

    for i in range(len(mymap)):
        if mymap[i] > 500:
            print(i, mymap[i])
    label_position = []


connected_components()
print('finished all image processing')


# In[ ]:




