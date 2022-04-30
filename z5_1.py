from sorting import select_qs, quickSort, dualPivotQuickSort, select_dqs
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import tqdm
import sys


def main():
    sys.setrecursionlimit(10000)
    sns.set()
    data = {}
    n_list = [100*i for i in range(1, 11)]
    data['quickSort'] = {}
    data['select_qs'] = {}
    data['dualPivotQuickSort'] = {}
    data['select_dqs'] = {}
    for n in tqdm.tqdm(n_list):
        data['quickSort'][n] = [0, 0]
        data['select_qs'][n] = [0, 0]
        data['dualPivotQuickSort'][n] = [0, 0]
        data['select_dqs'][n] = [0, 0]
        for _ in range(100):
            a = np.random.permutation(n)
            b = np.copy(a)
            c, s = select_qs(b)
            data['select_qs'][n][0] += c
            data['select_qs'][n][1] += s
            b = np.copy(a)
            c, s = quickSort(b, 0, len(b)-1)
            data['quickSort'][n][0] += c
            data['quickSort'][n][1] += s
            b = np.copy(a)
            c, s = dualPivotQuickSort(b, 0, len(b)-1)
            data['dualPivotQuickSort'][n][0] += c
            data['dualPivotQuickSort'][n][1] += s
            b = np.copy(a)
            c, s = select_dqs(b)
            data['select_dqs'][n][0] += c
            data['select_dqs'][n][1] += s
        data['select_qs'][n][0] /= 100
        data['select_qs'][n][1] /= 100
        data['quickSort'][n][0] /= 100
        data['quickSort'][n][1] /= 100
        data['dualPivotQuickSort'][n][0] /= 100
        data['dualPivotQuickSort'][n][1] /= 100
        data['select_dqs'][n][0] /= 100
        data['select_dqs'][n][1] /= 100

    plt.title('comparisons')
    plt.plot(n_list, [data['select_qs'][n][0] for n in n_list], label='select_qs')
    plt.plot(n_list, [data['quickSort'][n][0] for n in n_list], label='quickSort')
    plt.plot(n_list, [data['dualPivotQuickSort'][n][0] for n in n_list], label='dualPivotQuickSort')
    plt.plot(n_list, [data['select_dqs'][n][0] for n in n_list], label='select_dqs')
    plt.legend()
    plt.savefig('z5_1_comparisons.png')
    plt.clf()
    plt.title('swaps')
    plt.plot(n_list, [data['select_qs'][n][1] for n in n_list], label='select_qs')
    plt.plot(n_list, [data['quickSort'][n][1] for n in n_list], label='quickSort')
    plt.plot(n_list, [data['dualPivotQuickSort'][n][1] for n in n_list], label='dualPivotQuickSort')
    plt.plot(n_list, [data['select_dqs'][n][1] for n in n_list], label='select_dqs')
    plt.legend()
    plt.savefig('z5_1_swaps.png')
    plt.clf()


if __name__ == '__main__':
    main()
