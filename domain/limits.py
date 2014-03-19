#!/usr/bin/python
# -*- coding: utf-8 -*-
#****************************************************************#
# ScriptName: test.py
# Author: 
# Create Date: 2014-03-07
# Modify Author: 
# Modify Date: 2014-03-07
# Function: 
#***************************************************************#
import execs
import random
def conf_limits():
    cmd=["grid   soft   nofile    1024","grid   hard   nofile    65536","grid   soft   nproc    2047","grid   hard   nproc    16384","grid   soft   stack    10240","grid   hard   stack    32768","oracle   soft   nofile    1024","oracle   hard   nofile    65536","oracle   soft   nproc    2047","oracle   hard   nproc    16384","oracle   soft   stack    10240","oracle   hard   stack    32768"]
    f=open('/etc/security/limits.conf','a');
    for i in range(0,len(cmd)):
        f.write(cmd[i]+"\n")
    f.close()
    print "limits is configure               \033[1;32;40m ok\033[0m "
if __name__ == "__main__":
    conf_limits()

