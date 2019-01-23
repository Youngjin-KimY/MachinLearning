import numpy as np
from scipy.spatial.distance import pdist,squareform
from scipy.misc import imread, imsave, imresize

img = imread('cat.jpg')
print(img.dtype,img.shape)

img_tinted = img * [0,2,2]

img_tinted = imresize(img_tinted,(300,300))

imsave('cat_tinted.jpg',img_tinted)

print("---------------------------------------------------------")

x = np.array([[0,1],[1,0],[2,0]])
print(x)