#!/usr/bin/python
# -*- coding: utf-8 -*-
#****************************************************************#
# ScriptName: install.py
# Author: 
# Create Date: 2014-03-07
# Modify Author: 
# Modify Date: 2014-03-07
# Function: 
#***************************************************************#
import domain.firewall
import domain.selinux
import domain.adduser
import domain.grid_profile
import domain.limits
import domain.mkdir
import domain.oracle_profile
import domain.sysctl
import domain.rpm
print '\033[1;31;40m'
print '*' * 50
print "---------category---------   ----Result----"
print '\033[0m'
domain.firewall.stop_firewall()
domain.selinux.stop_selinux()
domain.adduser.add_user()
#domain.grid_profile.conf_grid()
domain.limits.conf_limits()
domain.mkdir.mkopt()
domain.oracle_profile.conf_oracle()
domain.sysctl.conf_sysctl()
domain.rpm.yum_install()
print '\033[1;31;40m'
print '*' * 50
print '\033[0m'
