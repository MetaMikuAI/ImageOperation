#Drag at least one Image has an identical height onto it, then they will be pasted laterally to a BIG IMAGE named 'output.jpg'.
#If only one Image input， python will convert input Image in all supported format into '.jpg'
import numpy as np
from PIL import Image
import sys
n=0
for arg in sys.argv:
    if n==0:
        n+=1
        continue
    if n==1:
        im=np.array(Image.open(sys.argv[n]))
        n+=1
    else:
        im=np.concatenate((im,np.array(Image.open(sys.argv[n]))),axis=1)
        n+=1

img=Image.fromarray(im)
img.save('out.jpg')
