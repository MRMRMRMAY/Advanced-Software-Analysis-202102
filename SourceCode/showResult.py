import matplotlib.pyplot as plt
import numpy as np

def load_data(fileName):
    X = np.loadtxt(fileName, delimiter=' ');
    return X;
X = load_data("./centroid_blobs_ILP.txt")
centers = load_data("./centers_second.txt")
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(X[:,0], X[:,1], c='black', marker='x', s = 1)
print(len(centers))
for center in centers:
    disk1 = plt.Circle((center[0], center[1]), 100, color='black', fill=False)
    ax.add_artist(disk1)
plt.show();