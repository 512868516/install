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
def conf_grid():
    cmd=["export ORACLE_BASE=/opt/ogrid","export ORACLE_HOME=/opt/grid/products/11.2.0","export PATH=$PATH:$ORACLE_HOME/bin","export ORACLE_SID=+ASM1","export PATH=$PATH:$ORACLE_HOME/bin","umask 022"]
    f=open('/home/grid/.bash_profile','a');
    for i in range(0,len(cmd)):
        f.write(cmd[i]+"\n")
    f.close()
    (stdout,stderr)=execs.call("source /home/grid/.bash_profile")
    (stdout,stderr)=execs.call("chown -R grid:oinstall /home/grid")
    print "grid profile is config            \033[1;32;40m ok\033[0m "
if __name__ == "__main__":
    conf_grid()
