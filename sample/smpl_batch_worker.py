# -*- coding: utf-8 -*-

__author__ = "Meritz"
__date__ = "creation: 2021-03-06, modification: 0000-00-00"

#################
#import
#################

import sys
from conf import config

def do_sample_file():
    print("do something")
    with open(sys.argv[1],'r') as fp:
        lines = fp.readlines()

    #print(lines)

    cnt=0
    step=0
    file_dict = dict()
    content=""
    for line in lines:
        if(line.strip() == "[[MKMS_META]]"):
           #print("meta-->",line)
           step=1
        elif (line.strip() == "[[MKMS_CONTENT]]"):
            #print("content-->",line)
            step = 2

        #print("line--->", cnt, "----> ", line)
        if(step==1):
            if(line.startswith("ID:")):
                file_dict["ID"] = line[3:].strip()
            elif(line.startswith("SUBJECT:")):
                file_dict["SUBJECT"] = line[8:].strip()
            elif(line.startswith("URL:")):
                file_dict["URL"] = line[4:].strip()
            else:
                #print("err step1 -> ",line)
                pass
        elif(step==2):
            if(line.strip() != "[[MKMS_CONTENT]]"):
                content = content + line

        cnt = cnt + 1

    file_dict["CONTNET"] = content
    print(file_dict)

    return file_dict

def do_sample_anal(file_dict):
    for k,v in file_dict.items():
        print(k)
        print(v)

def do_sample_elastic(file_dict):
    for k,v in file_dict.items():
        print(k)
        print(v)

def main():
    print("argv : ", sys.argv)
    file_dict = do_sample_file()
    do_sample_anal(file_dict)
    do_sample_elastic(file_dict)

if __name__ == "__main__":
    print("Im Worker")
    main()
