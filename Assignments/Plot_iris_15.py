# This program compares different linear SVM classifiers on a 2D projection
# (x,y) of the prominent 'iris' dataset. 
# Four SVM classifiers are used here with different kernels.

# import the required libraries:
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
#############################################################################
# define a function named meshgrid to create a mesh with parameters (x,y) 
# and a height having a stepsize of 0.2 (interval length):
def make_meshgrid(x, y, h=.02):
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    return xx, yy # returns xx and yy n-dimensional (nd) arrays
#############################################################################
# we define a method to plot the decision boundaries for a classifier,
# which takes input parameters of an axes object, a classifier, two meshgrid
# nd arrays (returned from make_meshgrid()) and optionally a dictionary of 
# params to pass contourf:
# (the ** operator allows us to take a dictionary of key-value pairs and 
# unpack it into keyword arguments in a function call)
def plot_contours(ax, clf, xx, yy, **params):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out
#############################################################################
# import the pre-existent iris dataset, which contains information 
# about the iris flower (including petal and sepal length):
iris = datasets.load_iris()

# get the first two features by constructing a two-dimensional dataset:
X = iris.data[:, :2]
y = iris.target

# creating an instance of SVM and fitting our data, with no scaling so we can
# plot the support vectors:
C = 1.0  # SVM regularization parameter
models = (svm.SVC(kernel='linear', C=C),
          svm.LinearSVC(C=C),
          svm.SVC(kernel='rbf', gamma=0.7, C=C),
          svm.SVC(kernel='poly', degree=3, C=C))
# get the models on (x,y) meshgrid with different classifiers:
models = (clf.fit(X, y) for clf in models)

# assign corresponding titles for the four different plots:
titles = ('SVC with linear kernel',
          'LinearSVC (linear kernel)',
          'SVC with RBF kernel',
          'SVC with polynomial (degree 3) kernel')

# Set-up a 2x2 grid for our plots:
fig, sub = plt.subplots(2, 2)
plt.subplots_adjust(wspace=0.4, hspace=0.4)

X0, X1 = X[:, 0], X[:, 1]
xx, yy = make_meshgrid(X0, X1)

# run a loop through the (4) different classifiers, their corresponding titles
# and axes using zip() (which returns an iterator from the mentioned iterables)
# with the models and titles passed in arguments following a call to flatten()
# which returns a copy of those array values collapsed in one dimension: 
for clf, title, ax in zip(models, titles, sub.flatten()):
    plot_contours(ax, clf, xx, yy,
                  cmap=plt.cm.coolwarm, alpha=0.8)
    ax.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xlabel('Sepal length')
    ax.set_ylabel('Sepal width')
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_title(title)
# display the plot:
plt.show()
