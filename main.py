import dataset
X,Y = dataset.load_linear_example1()
print(X)
print(X[0])
print(Y)

import regression
model = regression.LinearRegression()
print(model.x)

import importlib
importlib.reload(regression)
model = regression.LinearRegression()
model.fit(X,Y)
print(model.theta)

importlib.reload(regression)
model = regression.LinearRegression()
model.fit(X,Y)
print(model.predict(X))

importlib.reload(regression)
model = regression.LinearRegression()
model.fit(X,Y)
print(model.score(X,Y))