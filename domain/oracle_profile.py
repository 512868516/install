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
def conf_oracle():
    cmd=["export ORACLE_BASE=/opt/oracle","export ORACLE_HOME=$ORACLE_BASE/products/11.2.0","export PATH=$PATH:$ORACLE_HOME/bin","export ORACLE_SID=db1","export NLS_LANG=AMERICAN_AMERICA.ZHS16GBK","umask 022","alias sqlplus='rlwrap sqlplus'","alias rman='rlwrap rman'"]
    f=open('/home/oracle/.bash_profile','a');
    for i in range(0,len(cmd)):
        f.write(cmd[i]+"\n")
    f.close()
    (stdout,stderr)=execs.call("source /home/oracle/.bash_profile")
    (stdout,stderr)=execs.call("chown -R oracle:oinstall /home/oracle")
    print "oracle profile is config          \033[1;32;40m ok\033[0m "
if __name__ == "__main__":
    conf_oracle()

