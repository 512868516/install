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
def add_user():
    cmd=["/usr/sbin/groupadd -g 501 oinstall","/usr/sbin/groupadd -g 502 dba","/usr/sbin/groupadd -g 503 oper","/usr/sbin/groupadd -g 504 asmadmin","/usr/sbin/groupadd -g 505 asmoper","/usr/sbin/groupadd -g 506 asmdba","/usr/sbin/useradd -g oinstall -G dba,asmdba  oracle","/usr/sbin/useradd -g oinstall -G asmadmin,asmdba,dba grid","echo 'oracle' | passwd oracle --stdin","echo 'grid' | passwd grid --stdin"]
    for i in range(0,len(cmd)):
        (stdout,stderr)=execs.call(cmd[i])
    print "user add is                       \033[1;32;40m ok \033[0m"
if __name__ == "__main__":
    add_user()

