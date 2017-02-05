from scipy import misc
import numpy as np
from matplotlib import pyplot as plt 
path = 'pic2.png'
img = misc.imread(path).astype(np.float)
outf = open(path+".txt",'w')

print 'image shape',img.shape

grayimg = np.dot(img[...,:3],[0.299, 0.587, 0.144]) 
print 'gray image shape',grayimg.shape

H = grayimg.shape[0]
W = grayimg.shape[1]
gm = grayimg
##################
X = int(2*70*W/H)

print W,H,70,X
plt.imshow(grayimg,cmap=plt.get_cmap("gray"))
plt.show()

for i in range(70):
    for j in range(X):
	val = gm[i*H/70][j*W/X]
	if val < 80 : 
	    outf.write(' ')
	elif val < 100:
		outf.write('.')
	elif val <160 :
		outf.write('-')
	elif val < 175:
		outf.write('*')
	elif val < 190:
		outf.write('X')
	elif val < 205:
	    outf.write('O')
	elif val < 220:
		outf.write('0')
	else :
	    outf.write('8')

    outf.write('\n')


'''    .," -oO0@   '''