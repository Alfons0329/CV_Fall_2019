# Computer Vision HW5, Gray Scale Morphology Report
###### tags: `NTU CS` `Computer Vision` `Writeup` `Report`
NTU CSIE, R08922024, Alfons Hwu
Prequisites and env as the following
```
Ubuntu WSL for windows with jupyter notebook
Python3.6.7
OpenCV for image IO 
Matplotlib for displaying image
```

## a, dilation
By definition from [wikipedia](https://en.wikipedia.org/wiki/Dilation_(morphology)), use the probing kernel to search for the supremum of neighbour pixels.

$$(f\oplus b)(x)=\sup _{{y\in E}}[f(y)+b(x-y)]$$
```python
def dilation(a, b):
    ra, ca = a.shape # original image
    res = np.zeros(a.shape, dtype = 'int32')
    
    for ai in range(ra):
        for aj in range(ca):
                
                max_value = 0
                for b_each in b:
                    bi, bj = b_each
                    if  ai + bi >= 0 and ai + bi < ra\ 
                    and aj + bj >= 0 and aj + bj < ca: 
                        # extend the value
                        max_value = max(max_value, a[ai + bi, aj + bj])
                
                res[ai, aj] = max_value 
                        
    return res 
```
![](https://i.imgur.com/SbnddjK.png)
Time complexity, kernel size $K: O(MNK)$

## b, erosion

By definition from [wikipedia](https://en.wikipedia.org/wiki/Erosion_(morphology)), use the probing kernel to search for the infimum of neighbour pixels.

$$(f\ominus b)(x)=\inf _{{y\in B}}[f(x+y)-b(y)],$$

```python
def erosion(a, b):
    ra, ca = a.shape # original image
    res = np.zeros(a.shape, dtype = 'int32')
    
    for ai in range(ra):
        for aj in range(ca):
                
                min_value = 0x100
                for b_each in b:
                    bi, bj = b_each
                    if  ai + bi >= 0 and ai + bi < ra\  
                    and aj + bj >= 0 and aj + bj < ca: 
                        # extend the value
                        min_value = min(min_value, a[ai + bi, aj + bj])
                    
                res[ai, aj] = min_value
    
    return res 
```
![](https://i.imgur.com/AKUIWSY.png)
Time complexity, kernel size $K: O(MNK)$

## c, opening
```python
def opening(a, b):
    return dilation(erosion(a, b), b)
```
![](https://i.imgur.com/AbFKFLU.png)

Time complexity, kernel size $K: O(MNK)$

## d, closing
```python
def closing(a, b):
    return erosion(dilation(a, b), b)
```
![](https://i.imgur.com/voTsmRm.png)

Time complexity, kernel size $K: O(MNK)$
