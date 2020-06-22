from sklearn import datasets
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
iris=datasets.load_iris()
print(list(iris.keys()))
print(iris['data'])
print(iris['target'])
x=iris["data"][:,3:]
y=(iris["target"]==2)
print(y)
print(x)
clf=LogisticRegression()
clf.fit(x,y)
example=clf.predict(([[2.6]]))
print(example)
# plotting
X=np.linspace(0,3,1000).reshape(-1,1)
print(X)
y_prob=clf.predict_proba(X)
plt.plot(X,y_prob[:,1],"g-",label="virginica")
plt.show()