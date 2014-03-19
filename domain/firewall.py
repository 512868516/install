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
def stop_firewall():
    cmd=["chkconfig iptables off","service iptables stop"]
    for i in range(0,len(cmd)):
        (stdout,stderr)=execs.call(cmd[i])
    print "firewall stop                     \033[1;32;40m ok \033[0m"
if __name__ == "__main__":
    stop_firewall()

