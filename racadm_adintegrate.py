#!/usr/bin/python

import os

import commands

# Open a file - Input file for IDRAC Push

fo = open("ip.txt", "r")

for ip in fo:

        ip = ip.strip()

        print ('Performing remote IDRAC Operations on -> %s' %ip)

	m=['racadm config -g cfgLanNetworking -o cfgDNSDomainName <domain name>','racadm config -g cfgLanNetworking -o cfgDNSServer1 <ip>','racadm config -g cfgActiveDirectory -o cfgADEnable 1','racadm config -g cfgActiveDirectory -o cfgADType 2','racadm config -g cfgUserDomain -o cfgUserDomainName <domain name> -i 1','racadm config -g cfgActiveDirectory -o cfgADDomainController1 <domain name>','racadm config -g cfgActiveDirectory -o cfgADGlobalCatalog1 <domain name>','racadm config -g cfgStandardSchema -i 1 -o cfgSSADRoleGroupName iDRAC-Administrators','racadm config -g cfgStandardSchema -i 2 -o cfgSSADRoleGroupName iDRAC-Operators','racadm config -g cfgStandardSchema -i 3 -o cfgSSADRoleGroupName iDRAC-Readonly','racadm config -g cfgStandardSchema -i 1 -o cfgSSADRoleGroupDomain <domain>','racadm config -g cfgStandardSchema -i 2 -o cfgSSADRoleGroupDomain <domain>','racadm config -g cfgStandardSchema -i 3 -o cfgSSADRoleGroupDomain <domain>','racadm config -g cfgStandardSchema -i 1 -o cfgSSADRoleGroupPrivilege 0x000001ff','racadm config -g cfgStandardSchema -i 2 -o cfgSSADRoleGroupPrivilege 0x000000f9','racadm config -g cfgStandardSchema -i 3 -o cfgSSADRoleGroupPrivilege 0x00000001']

	for j in m:	
		o1 = commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s '%s'"%(ip,j))



        print o1


fo.close()

