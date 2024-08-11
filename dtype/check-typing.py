#!/usr/bin/env python3
import time
import random

from typing import List


def init() ->  List[float]:

    random.seed(time.time())
    n_list = 1024 * 1024 * 1024
    z = [0.] * n_list

    print ('start for')
    for i in range(n_list):
        if 0 == i % 100000:
            print('|', end='', flush=True)
        x = random.random()
        z[i] = x


    return z


if __name__ == "__main__":

    v: List[float]

    v = init()

    for i in range(len(v)-10, len(v)):
        print (v[i])

    print ('-'*100, flush=True)
    while True:
        time.sleep(100000)
