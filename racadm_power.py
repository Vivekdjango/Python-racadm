#!/usr/bin/python

import os

import commands


# Open a file - Input file for IDRAC Push

fo = open("ip.txt", "r")


for ip in fo:

        ip = ip.strip()

        print ('Performing remote IDRAC Operations on -> %s' %ip)

	o1 = commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm serveraction powerup'" % ip)

	print o1

fo.close()

