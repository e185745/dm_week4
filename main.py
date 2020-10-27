import dataset
X,Y = dataset.load_linear_example1()
print(X)
print(X[0])
print(Y)

import regression
model = regression.LinearRegression()
print(model.x)