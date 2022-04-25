from functions import random_select
import sys


def main():
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    arr = [int(sys.stdin.readline()) for _ in range(n)]
    print('before select:', arr)
    x, c, s = random_select(arr, k, n < 50)
    print('after select:', arr)
    print(f'{k}-ta statystyka pozycyjna:', x)
    arr.sort()
    print('posortowana tablica:', arr)
    print(f'arr[{k}] = {arr[k]}')
    print(f'ilość porównań: {c}')
    print(f'ilość przestawień: {s}')


if __name__ == '__main__':
    main()
