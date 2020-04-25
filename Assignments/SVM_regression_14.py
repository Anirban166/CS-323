# importing required libraries:
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
#############################################################################
# Generating random sample data with np.random.rand(), sorted via 
# np.sort()'s sorting mechanism/functionality on aligned axis, and 
# assigning the array so formed into a variable:
X = np.sort(5 * np.random.rand(40, 1), axis=0)
# note we can change the sorting mechanism by specifying the required
# sorting method via kind = "xyzsort".

# similarly, np.six(X).ravel() is used to create a contiguous flattened
# array with the corresponding sine values of X[].
y = np.sin(X).ravel()
# print those values:
print (X)
print (y)
#############################################################################
y[::5] += 3 * (0.5 - np.random.rand(8))
print (y)
# adds noise, with:
# y[::5] returning every second entry in list y
# += (compound addition assignment) adding the value to the right of =
# np.random.rand() generating random samples from a uniform distribution
# of [0,1), similar to std::uniform_distribution in C++ (or rand() function)

#############################################################################
# fit regression models with corresponding kernels 
# and parameter specifications:
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_lin = SVR(kernel='linear', C=1e3)
svr_poly = SVR(kernel='poly', C=1e3, degree=2)
y_rbf = svr_rbf.fit(X, y).predict(X)
y_lin = svr_lin.fit(X, y).predict(X)
y_poly = svr_poly.fit(X, y).predict(X)
#############################################################################
# display the results via a plot, for which we specify the needful:
lw = 2
# use a scatterplot to display our data points (X,y), 
# with darkorange colour and a label (text) of 'data':
plt.scatter(X, y, color='darkorange', label='data')
# display the other values (X,other) where other refers to y_rbf, y_lin,
# y_poly with different colors and labels to distinguish:
plt.plot(X, y_rbf, color='navy', lw=lw, label='RBF model')
plt.plot(X, y_lin, color='c', lw=lw, label='Linear model')
plt.plot(X, y_poly, color='cornflowerblue', lw=lw, label='Polynomial model')
# give names to x and y axis labels in the plot:
plt.xlabel('data')
plt.ylabel('target')
# assign a title as well: (shown at the top)
plt.title('Support Vector Regression')
# assign the legend and display the plot:
plt.legend()
plt.show()
