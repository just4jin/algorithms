import numpy as np
import scipy
import matplotlib
import sklearn

#%pylab inline
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.datasets.samples_generator import make_blobs

##************************
##     Numpy
##************************

# Generating a random array
X = np.random.random((3,5)) # a 3 x 5 array
print X

# Accessing elements

# get a single element
print X[0,0]

# get a row
print X[1]

# get a column
print X[:,1]

# transpose an array
print X.T

# turning a row vector into a column vector
y = np.linspace(0,12,5)
print y

# make into a column vector
print y[:,np.newaxis]

##*************************
## scipy sparse matrices
##************************

# textual analysis
from scipy import sparse

# create a random array with a lot of zeros
X = np.random.random((10,5))
print X
X[X<0.7]=0
print X

# turn X into a csr (Compressed-Sparse-Row) matrix
X_csr = sparse.csr_matrix(X)
print X_csr

# convert the sparse matrix to a dense array
print X_csr.toarray()
# CSR representation can be very efficient for computations, not 
# so good for adding elements, where List-In-List representation is better

# create an empty LIL matrix and add some items
X_lil = sparse.lil_matrix((5,5))

for i,j in np.random.randint(0,5,(15,2)):
    X_lil[i,j] = i + j
    
print X_lil
print X_lil.toarray()

# convert to a csr format 
X_csr = X_lil.tocsr()
print X_csr

# Useful sparse formats
# - CSC compressed sparse column
# - BSR block sparse row
# - COO coordinate
# - DIA diagonal
# - DOK dictionary of keys
# applications in linear algebra, sparse solvers, graph algorithms

##**************************
##      Matplotlib
##**************************
import matplotlib.pyplot as plt
# plot a line
x= np.linspace(0,10,100)
plt.plot(x,np.sin(x))

# scatter-plot
x = np.random.normal(size=500)
y = np.random.normal(size=500)
plt.scatter(x,y)

# showing images
x = np.linspace(1,12,100)
y = x[:,np.newaxis]
im = y*np.sin(x)*np.cos(y)
print im.shape

# imshow - note that origin is at the top left
plt.imshow(im)
# contour plot - note that origin here is at the bottom-left
plt.contour(im)
