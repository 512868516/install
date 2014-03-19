#!/usr/bin/python
# -*- coding: utf-8 -*-
#****************************************************************#
# ScriptName: call.py
# Author: 
# Create Date: 2014-03-07
# Modify Author: 
# Modify Date: 2014-03-07
# Function: 
#***************************************************************#
import subprocess
import string
def call(cmd):
    p = subprocess.Popen(cmd,\
            stdin  = subprocess.PIPE,\
            stdout = subprocess.PIPE,\
            stderr = subprocess.PIPE,\
            shell  = True);
    stdout,stderr = p.communicate();
    return stdout,stderr;
