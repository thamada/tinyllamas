#!/usr/bin/env python3
import time
import random
import sys
import numpy as np
from memory_profiler  import profile



@profile
def init():

    random.seed(time.time())
    n_list = 1024 * 1024 * 1024

    z = np.zeros(n_list, dtype=float)

    print ('start for')
    for i in range(n_list):

        if 0 == i % 100000:
            print('|', end='', flush=True)

        if 0 == i % 10000000:
            print ('', flush=True)
            print ("%d byte" %  sys.getsizeof(z), flush=True)
            print ("%d byte" %  z.nbytes, flush=True)


        x = random.random()
        z[i] = x


    return z


if __name__ == "__main__":

    v = init()

    for i in range(len(v)-10, len(v)):
        print (v[i])

    print ('-'*100, flush=True)

    '''
    while True:
        time.sleep(100000)
    '''
