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
def yum_install():
    cmd="yum install -y libcap*.i686 libcap*.x86_64 elfutils-libelf-devel*.i686  elfutils-libelf-devel*.x86_64 binutils*.x86_64 compat-libcap1++-*.x86_64 compat-libstdc++-*.x86_64 compat-libstdc++-*.i686 gcc-*.x86_64 gcc-c++-*.x86_64 glibc-*.i686  glibc-*.x86_64 glibc-devel-*.x86_64 glibc-headers-* glibc-devel-*.i686 ksh libgcc-*.i686  libgcc-*.x86_64 libstdc++-*.x86_64 libstdc++-*.i686 libstdc++-devel*.x86_64 libstdc++-devel*.i686 libaio*.x86_64 libaio*.i686 libaio-devel*.x86_64 libaio-devel*.i686 make sysstat*.x86_64 /tmp/CVU_11.2.0.3.0_grid/runfixup.sh"
    (stdout,stderr)=execs.call(cmd)
    stdout = stdout.split("\n")
    match = "Complete!"
    for i in range(0,len(stdout)):
        if i == 47:
            if match in stdout[i]:
                print "yum install is                    \033[1;32;40m Complete"
            else:
                print "yum install is                    \033[1;31;40m Error \033[0m"
        else:
            continue
if __name__ == "__main__":
    yum_install()

