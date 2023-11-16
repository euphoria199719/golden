import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris=pd.read_csv('iris.csv')
print(iris.head())
x=iris.drop("Species",axis=1)
y=iris["Species"]
print(x.head())
print(y.head())

STD=(x-x.mean())/x.std()
covariance=np.cov(STD,rowvar=False)
print(STD.head())
print("Covariance Matrix")
print(covariance)
evalue,evector=np.linalg.eig(covariance)
print("Eigen Value")
print(evalue)
print("Eigen Vector")
print(evector)
index=np.argsort(evalue)[::-1]
evalue=evalue[index]
evector=evector[:,index]
n=2
projection=STD.dot(evector[:,:n])
print(projection)
plt.figure(figsize=(8,6))
for species in iris['Species'].unique():
    plt.scatter(projection[y == species, 0],projection[y == species, 1],label=species)
    
plt.xlabel("Principal component 1")
plt.ylabel("Principal component 2")
plt.legend()
plt.title("PCA of IRIS data")
plt.show()




