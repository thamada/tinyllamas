#!/usr/bin/env python3
import time
import random
import sys
from memory_profiler  import profile


def init():

    random.seed(time.time())
    n_list = 1024 * 1024 * 1024
    z = [0.] * n_list

    for i in range(n_list):

        if 0 == i % 100000:
            print('|', end='', flush=True)

        x = random.random()
        z[i] = x

    return z


@profile
def main():
    v = init()

    for i in range(len(v)-10, len(v)):
        print (v[i])

    print ('-'*100, flush=True)

'''
    while True:
        time.sleep(120)
'''

if __name__ == "__main__":

    main()
