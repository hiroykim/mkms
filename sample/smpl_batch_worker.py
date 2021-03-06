# -*- coding: utf-8 -*-

__author__ = "Meritz"
__date__ = "creation: 2021-03-06, modification: 0000-00-00"

#################
#import
#################

import sys
from conf import config

def do_sample():
    print("do something")
    with open(sys.argv[1],'r') as fp:
        all = fp.read()

    print(all)

def main():
    print("argv : ", sys.argv)
    do_sample()

if __name__ == "__main__":
    print("Im Worker")
    main()
