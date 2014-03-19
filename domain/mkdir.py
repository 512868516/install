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
def mkopt():
    cmd=["mkdir -p /opt/oracle/products/11.2.0","mkdir -p /opt/oracle/diag","mkdir -p /opt/ogrid","mkdir -p /opt/grid/products/11.2.0","mkdir -p /opt/grid/oraInventory","chown -Rf oracle:oinstall /opt/oracle","chown -Rf grid:oinstall /opt/grid","chown -Rf grid:oinstall /opt/ogrid","chown -Rf grid:oinstall /opt/grid/oraInventory"]
    for i in range(0,len(cmd)):
        (stdout,stderr)=execs.call(cmd[i]);
    print "mkdir is configure                \033[1;32;40m ok\033[0m"
if __name__ == "__main__":
    mkopt()
