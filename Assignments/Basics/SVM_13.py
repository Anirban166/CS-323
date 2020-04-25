# import svm from the machine learning library scikit-learn or sklearn:
from sklearn import svm

# assigning values to two variables (X,y) for future use:
X = [[0, 0], [1, 1]]
y = [0, 1]
# printing them:
print(X)
print(y)

# using sklearn.svm.SVC() for C-support vector classification,
# where rbf kernel type is specified 
# (which is the default kernel specification) 
# and iteration limit is set to 100:
clf = svm.SVC(kernel='rbf', max_iter=100) 

# using the classification to fit our model with (X,y) values:
clf.fit(X, y)   

# printing a variable which returns the prediction as per our model:
p=clf.predict([[2., 2.]])
print(p)

