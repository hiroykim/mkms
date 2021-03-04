# -*- coding: utf-8 -*-

__author__ = "Meritz"
__date__ = "creation: 2021-03-02, modification: 0000-00-00"

#################
#import
#################

import os
from time import sleep
import sys

def main():
    cnt = 0

    fp = open("/logs/mkms/hello_loop.log",'a')
    while True:
        v_str = "hello python -> " + str(cnt) +"\n"
        print(v_str)
        fp.write(v_str)
        sleep(1)
        cnt = cnt + 1
        fp.flush()
    close(fp)

if __name__ == "__main__":
    main()
