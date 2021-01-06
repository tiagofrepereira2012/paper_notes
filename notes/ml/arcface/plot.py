# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np

def plot_scatter(X, y):

    from sklearn.manifold import TSNE
    X_ = TSNE(n_components=3).fit_transform(X)

    labels = set(y)   
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for label in labels:
        indexes = np.where(y==label)[0]
        scatter = X_[indexes,:]  
        ax.scatter(scatter[:,0], scatter[:,1], scatter[:,2])

    plt.show()  