import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
data = pd.read_csv('iris.csv')

# Convert selected columns to numeric, handling errors with 'coerce'
columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
data[columns] = data[columns].apply(pd.to_numeric, errors='coerce')

# Calculate the correlation matrix
correlation = data.corr()
print(correlation)

# Outlier removal based on IQR
ot = 3
for col in columns:
    q1 = data[col].quantile(0.25)
    q3 = data[col].quantile(0.75)
    iqr = q3 - q1
    lb = q1 - ot * iqr
    ub = q3 + ot * iqr
    data = data[(data[col] >= lb) & (data[col] <= ub)]

# Plotting boxplots and histograms
fig, axes = plt.subplots(nrows=2, ncols=len(columns), figsize=(15, 8))

for i, col in enumerate(columns):
    # Boxplot
    data.boxplot(column=col, ax=axes[0, i])
    axes[0, i].set_title(f'Boxplot of {col}')

    # Histogram
    data[col].hist(bins=10, ax=axes[1, i])
    axes[1, i].set_title(f'Histogram of {col}')

plt.tight_layout()
plt.show()

# Visualization of the correlation matrix
plt.imshow(correlation, cmap='viridis', interpolation='none')
plt.colorbar()
plt.xticks(range(len(correlation)), correlation.columns, rotation=90)
plt.yticks(range(len(correlation)), correlation.columns)
plt.show()

# Descriptive statistics visualization
stats = data[columns].describe().transpose()
stats.plot(y=['mean', '50%', 'std', 'min', 'max'], kind='bar', legend=True)
plt.show()

# Histograms of selected columns
data[columns].hist(bins=10, figsize=(10, 8))
plt.legend(loc='upper right')
plt.show()

# K-Means Clustering
n_clusters = 3
np.random.seed(42)
centroids = data[columns].sample(n_clusters).values

for _ in range(100):
    distance = np.linalg.norm(data[columns].values[:, np.newaxis] - centroids, axis=2)
    labels = np.argmin(distance, axis=1)
    for i in range(n_clusters):
        centroids[i] = data[columns][labels == i].mean().values

data['cluster'] = labels

# Scatter plot for K-Means Clustering
colors = ['r', 'g', 'b']
for cluster, color in zip(range(n_clusters), colors):
    clustered_data = data[data['cluster'] == cluster]
    plt.scatter(clustered_data['SepalLengthCm'], clustered_data['SepalWidthCm'], c=color, label=f'Cluster {cluster}')

plt.xlabel('SepalLengthCm')
plt.ylabel('SepalWidthCm')
plt.legend()
plt.show()
