# -*- coding: utf-8 -*-

__author__ = "Meritz"
__date__ = "creation: 2021-03-06, modification: 0000-00-00"

#################
#import
#################
import subprocess
from conf import config

def sub_process(cmd):
    sub_pro = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # subprocess 가 끝날대까지 대기
    response_out, response_err = sub_pro.communicate()
    if len(response_out) > -1:
        print(response_out)
    if len(response_err) > -1:
        print(response_err)
    return response_out

def do_sample():
    print("do sample")
    cmd = "python /application/mkms/sample/smpl_batch_worker.py {0}/{1}".format(MKMSConfig.cfg_data_loc, test_data)
    print("cmd : ", cmd)
    sub_process(cmd)

def main():
    print("Hello Python!")
    do_sample()


if __name__ == "__main__":
    MKMSConfig = config.MKMSConfig
    test_data="sample_data.dat"
    main()
