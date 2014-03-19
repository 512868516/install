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
def conf_sysctl():
    cmd=["fs.aio-max-nr = 1048576","fs.file-max = 6815744","kernel.shmall = 2097152","kernel.shmmax = 4294967295","kernel.shmmni = 4096","kernel.sem = 250 32000 100 128","net.ipv4.ip_local_port_range = 9000 65500","net.core.rmem_default = 262144","net.core.rmem_max = 4194304","net.core.wmem_default = 262144","net.core.wmem_max = 1048576"]
    f=open('/etc/sysctl.conf','a');
    for i in range(0,len(cmd)):
        f.write(cmd[i]+"\n")
    f.close()
    (stdout,stderr)=execs.call("/sbin/sysctl -p")
    if stdout!=" ":
        print "sysctl is configure               \033[1;32;40m ok\033[0m"
if __name__ == "__main__":
    conf_sysctl()

