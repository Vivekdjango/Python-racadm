#!/usr/bin/python

import os

import commands

# Open a file - Input file for IDRAC Push

fo = open("ip.txt", "r")

for ip in fo:

        ip = ip.strip()

        print ('Performing remote IDRAC Operations on -> %s' %ip)

	#Updating TZ

	o1=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm set idrac.time.timezone Etc/UTC'" % ip)

	#Updating NTP details

	o2=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm set iDRAC.NTPConfigGroup.NTP1 0.pool.ntp.org'" % ip)

	o3=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm set iDRAC.NTPConfigGroup.NTP2 1.pool.ntp.org'" % ip)

	o4=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm set iDRAC.NTPConfigGroup.NTP3 2.pool.ntp.org'" % ip)

	o5=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm set iDRAC.NTPConfigGroup.NTPEnable 1'" % ip)


        update = open("tz.txt", "a")

        print o1,o2,o3,o4,o5
        update.write(ip)
        update.write(o1)
        update.write(o2)
	update.write(o3)
	update.write(o4)
	update.write(o5)
        update.close()

# Close opend file

fo.close()

