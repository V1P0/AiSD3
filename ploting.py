import matplotlib.pyplot as plt
import tqdm
import random
from functions import *


def plot_3d(x, y, z, x_label, y_label, z_label, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)
    ax.set_title(title)
    plt.show()


def main():
    ns = [100*i for i in range(1, 101)]
    results = [[0 for _ in range(100)] for _ in range(100)]
    m = 1
    for i in tqdm.tqdm(range(100)):
        for j in range(100):
            for _ in range(m):
                arr = [random.randint(0, 2*ns[i]-1) for _ in range(ns[i])]
                k = ns[i]//100*j
                results[i][j] += select(arr, k)[1]
            results[i][j] /= m
    x = []
    y = []
    z = []
    for i in range(100):
        for j in range(100):
            x.append(ns[i])
            y.append(ns[j])
            z.append(results[i][j])
    plot_3d(x, y, z, 'n', 'k', 'comparisons', 'comps')


if __name__ == "__main__":
    main()
