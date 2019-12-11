# Computer Vision HW10, Zero Crossing Edge Detection
###### tags: `NTU CS` `Computer Vision` `Writeup` `Report`
NTU CSIE, R08922024, Alfons Hwu
Prequisites and env as the following
```
Ubuntu WSL for windows with jupyter notebook
Python3.6.7
OpenCV for image IO 
Matplotlib for displaying image
```

## Laplace Mask1 (0, 1, 0, 1, -4, 1, 0, 1, 0): 15
Kernel
```python
k = np.array([
            [0, 1, 0],
            [1, -4, 1],
            [0, 1, 0]
        ])
```
![](https://i.imgur.com/RkURkDH.png)


## Laplace Mask2 (1, 1, 1, 1, -8, 1, 1, 1, 1): 15
Kernel
```python
k = np.array([
            [1, 1, 1],
            [1, -8, 1],
            [1, 1, 1]
        ])
```
![](https://i.imgur.com/CJBU2TJ.png)


## Minimum variance Laplacian: 20
Kernel
```python
k = np.array([
            [2, -1, 2],
            [-1, -4, -1],
            [2, -1, 2]
        ]) / 3
```
![](https://i.imgur.com/Z1aCqvU.png)


## Laplace of Gaussian: 3000
Kernel
```python
k = np.array([
            [0, 0, 0, -1, -1, -2, -1, -1, 0, 0, 0],
            [0, 0, -2, -4, -8, -9, -8, -4, -2, 0, 0],
            [0, -2, -7, -15, -22, -23, -22, -15, -7, -2, 0],
            [-1, -4, -15, -24, -14, -1, -14, -24, -15, -4, -1],
            [-1, -8, -22, -14, 52, 103, 52, -14, -22, -8, -1],
            [-2, -9, -23, -1, 103, 178, 103, -1, -23, -9, -2],
            [-1, -8, -22, -14, 52, 103, 52, -14, -22, -8, -1],
            [-1, -4, -15, -24, -14, -1, -14, -24, -15, -4, -1],
            [0, -2, -7, -15, -22, -23, -22, -15, -7, -2, 0],
            [0, 0, -2, -4, -8, -9, -8, -4, -2, 0, 0],
            [0, 0, 0, -1, -1, -2, -1, -1, 0, 0, 0]
        ])
```
![](https://i.imgur.com/aX14F3I.png)


## Difference of Gaussian: 1
Kernel
```python
k = np.array([
            [-1, -3, -4, -6, -7, -8, -7, -6, -4, -3, -1],
            [-3, -5, -8, -11, -13, -13, -13, -11, -8, -5, -3],
            [-4, -8, -12, -16, -17, -17, -17, -16, -12, -8, -4],
            [-6, -11, -16, -16, 0, 15, 0, -16, -16, -11, -6],
            [-7, -13, -17, 0, 85, 160, 85, 0, -17, -13, -7],
            [-8, -13, -17, 15, 160, 283, 160, 15, -17, -13, -8],
            [-7, -13, -17, 0, 85, 160, 85, 0, -17, -13, -7],
            [-6, -11, -16, -16, 0, 15, 0, -16, -16, -11, -6],
            [-4, -8, -12, -16, -17, -17, -17, -16, -12, -8, -4],
            [-3, -5, -8, -11, -13, -13, -13, -11, -8, -5, -3],
            [-1, -3, -4, -6, -7, -8, -7, -6, -4, -3, -1],
        ])
```
![](https://i.imgur.com/43beJr9.png)
