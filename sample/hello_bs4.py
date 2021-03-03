# -*- coding: utf-8 -*-

__author__ = "Meritz"
__date__ = "creation: 2021-03-02, modification: 0000-00-00"

#################
#import
#################
from bs4 import BeautifulSoup

def test():
    a = """
	<br>abcde</br>
	<br>bbcde</br>
	<br>cbcde</br>
	<br>dbcde</br>
        """
    print(a)

    a = BeautifulSoup(a, 'html5lib').get_text()
    print(a)

def main():
    test()

if __name__ == "__main__":
    main()
