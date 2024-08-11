#!/usr/bin/env python3
import time
import random
import sys

def getSize(array_byte):
    mb =  array_byte / (1024.*1024.)
    print ("%d Mbyte" %  mb, flush=True) 

def init():
    array_byte = 0

    random.seed(time.time())

    n_list = 1024 * 1024 * 1024
    z = [0.] * n_list

    array_byte += sys.getsizeof(z)

    print ('start for')
    for i in range(n_list):

        if 0 == i % 100000:
            print('|', end='', flush=True)

        if 0 == i % 10000000:
            getSize(array_byte)

        x = random.random()
        array_byte += sys.getsizeof(x)
        z[i] = x


    return z


if __name__ == "__main__":

    v = init()

    for i in range(len(v)-10, len(v)):
        print (v[i])

    print ('-'*100, flush=True)

    while True:
        time.sleep(100000)
