# for a 2D feature space plot the decision boundaries of a classifier
# X = input
# y = target (max. 3 classes)
# clf = sklearn classifier
def plot_decisions_2d(X, y, clf, resolution=0.02):
    from matplotlib.colors import ListedColormap
    import matplotlib.pyplot as plt
    import numpy as np
    shapes = ('o', 'v', 'x')
    colors = ('dodgerblue', 'darkorange', 'lightgreen')
    # we select as many colors as there are labels (no more than tree)
    # the result can be tuple in recent python versions, therefore has to be turned into a list
    cmap = ListedColormap(list(colors[:len(np.unique(y))]))
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
    np.arange(x2_min, x2_max, resolution))
    # xx1 are all the x1 coords of the points in a 2d grid
    # xx2 are all the x2 coords of the points in a 2d grid
    # creating an array we have two rows: xx1 coords and xx2 coords
    # transposing the array we get lots of rows each with an x1 and an x2 coord
    Z = clf.predict(np.array([xx1.reshape(-1), xx2.reshape(-1)]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    # plot actual points
    for idx, clazz in enumerate(np.unique(y)):
        plt.scatter(x=X[y == clazz, 0], y=X[y == clazz, 1],alpha=0.8,c=colors[idx],marker=shapes[idx],label=clazz)
