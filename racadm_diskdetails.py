#!/usr/bin/python

import os

import commands

import re

# Open a file - Input file for IDRAC Push

fo = open("ip.txt", "r")


ff=r'^FormFactor(.*)'
sn=r'^SerialNumber(.*)'
nm=r'^Name(.*)'
sz=r'^Size(.*)'

for ip in fo:

        ip = ip.strip()

        print ('Performing remote IDRAC Operations on -> %s' %ip)

	#Execute commands to get Physical Drive Details

	o1 = commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm raid get pdisks -o'" % ip)

	f=o1.split('\n')

	n=[]

	#Segerigate Data as per need

	for i in f:
		n.append(i.rstrip().lstrip())

	print ip+'\t'
	update = open("ff.txt", "a")
	update.write(ip+'\t')
	for j in n:
		if re.search(nm,j) or re.search(sn,j) or re.search(sz,j) or re.search(ff,j):	 
			print j
		        update = open("ff.txt", "a")
		        update.write(j+'\n')
		        update.close()

# Close opend file

fo.close()

