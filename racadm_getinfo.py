#!/usr/bin/python

import commands
import os


f=open("new_ip.txt","r")

print "IP"+'\t'+"DNS Name"+'\t'+"Bios"+"\t"+"iDRAC"+"\t"+"Boot Order"

#print "IP" + '\t'+"Bios"+"\t"+"iDRAC"
for i in f:
	i=i.strip()

	print "Working on",i

	a=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm get iDRAC.NIC.DNSRacName'"%i)
	DNS=a.split('\n')[-1].split('=')[1]

#	b=commands.getoutput("sshpass -p <password> ssh -o StrictHostkeyChecking=no root@%s 'racadm get Bios.MiscSettings.AssetTag'"%i)
#	Asset=b.split('\n')[-1].split('=')[1]


	#Get BIOS version
	c=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm getversion -f bios'"%i)
	bios=c.split()[3]

	#Get FW version

	d=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm getversion -f idrac'"%i)

	idrac=d.split()[3]

	#Get Bootorder

	boot=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm get BIOS.Biosbootsettings.bootseq'"%i)

	order=(boot.split('\n')[1].split('=')[1])

	print i+"\t"+DNS+"\t"+bios+"\t"+idrac+"\t"+order
#	print i + '\t'+bios+'\t'+idrac


	with open("get_data.txt","a") as g:
		g.write(i)
		g.write(DNS)
		g.write(bios)
		g.write(idrac)
		g.write(order)

