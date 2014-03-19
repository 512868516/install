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
def stop_selinux():
    content=["# This file controls the state of SELinux on the system.","# SELINUX= can take one of these three values:","#     enforcing - SELinux security policy is enforced.","#     permissive - SELinux prints warnings instead of enforcing.","#     disabled - No SELinux policy is loaded.","SELINUX=disabled","# SELINUXTYPE= can take one of these two values:","#     targeted - Targeted processes are protected,","#     mls - Multi Level Security protection.","SELINUXTYPE=targeted "]
    f=open('/etc/selinux/config','w')
    for i in range(0,len(content)):
        f.write(content[i]+"\n")
    f.close()
    print "selinux stop                      \033[1;32;40m ok \033[0m"
if __name__ == "__main__":
    stop_selinux()

