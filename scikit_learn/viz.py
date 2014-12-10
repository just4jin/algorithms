##***********************
##  Data in scikit-learn
##***********************

# data assumed to be 2-D
# size [n_samples, n_features]
# n_samples: each is an item to classify
#           a row in databse/csv file
# n_features: features to describe each item
# when features are millions of them, scipy.sparse
# can be useful, more memory efficient than numpy array

##**********************
##    Simple example
##**********************

# design an algorithm to recognize iris species
# load the iris data with scikit-learn

# features: -sepal length in cm -sepal width in cm
# -petal length in cm -petal width in cm
# target classes to predict: -iris setosa-iris versicolor
#-iris virginica

from sklearn.datasets import load_iris
iris = load_iris()
iris.keys()

# features of each sample flower stored in the data
n_samples, n_features = iris.data.shape
print n_samples #150
print n_features #4
print iris.data[0]

# information about the class of each sample 
# stored in the target attribute of the dataset
print iris.data.shape
print iris.target.shape
print iris.target
print iris.target_names # names of classes in last attribute

##############################################
##              Feature selection
##############################################

# this formatter will label colorbar with correct 
#target names

x_index = 0 # change to 2 is better
y_index = 1 # change to 3 is better 
formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

plt.scatter(iris.data[:, x_index], iris.data[:, y_index], c=iris.target)
plt.colorbar(ticks=[0, 1, 2], format=formatter)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index])

from sklearn import datasets
datasets.fetch_
datasets.load_

##*****************************
##      Loading digits data
##*****************************

# handwritten digits recognition
from sklearn.datasets import load_digits
digits = load_digits()
digits.keys()

n_samples, n_features = digits.data.shape
print (n_samples, n_features) #(1797, 64)
print digits.data[0]
print digits.target

print digits.data.shape#(1797, 64)
print digits.images.shape #(1797, 8, 8)

print np.all(digits.images.reshape((1797,64)) == digits.data) # True

## data visualization

##*********************************
##      handwritten digits
##*********************************
# set up the figure
fig = plt.figure(figsize=(6,6))#inch
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05,wspace=0.05)

# plot digits: each image is 8x8 pixels
for i in range(64):
    ax = fig.add_subplot(8,8,i+1,xticks=[],yticks=[])
    ax.imshow(digits.images[i],cmap=plt.cm.binary)
    
    # label the image with target value
    ax.text(0,7,str(digits.target[i])) # flattens 2d data to single vector

##***************************
##      faces dataset
##***************************

from sklearn.datasets import fetch_olivetti_faces
# fetch the faces data
faces = fetch_olivetti_faces()
faces.keys()

n_samples, n_features = faces.data.shape
print (n_samples, n_features) #(400, 4096)
print faces.data[0]
print faces.target

print faces.data.shape#(400, 4096)
print faces.images.shape #(400, 64, 64)

print np.all(faces.images.reshape((400,4096)) == faces.data) # True

# plot faces image data use plt.cm.bone for good colormap

# set up the figure
fig = plt.figure(figsize=(6,6))#inch
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05,wspace=0.05)

# plot faces: each image is 8x8 pixels
for i in range(64):
    ax = fig.add_subplot(8,8,i+1,xticks=[],yticks=[])
    ax.imshow(faces.images[i],cmap=plt.cm.bone)
    
    # label the image with target value
    ax.text(0,7,str(faces.target[i])) # flattens 2d data to single vector

### Note: sklearn forces each item to the same size
### getting the real-world cleaned to get recoginized
### ML needs the item to be the same measurements
