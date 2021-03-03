from khaiii import KhaiiiApi
# -*- coding: utf-8 -*-

__author__ = "Meritz"
__date__ = "creation: 2021-03-02, modification: 0000-00-00"

#################
#import
#################

import os

def test():
    api = KhaiiiApi()
    for word in api.analyze('아버지가 방에 들어가신다.'):
        print(word)


def main():
    print("Hello Python!")
    test()

if __name__ == "__main__":
    main()


