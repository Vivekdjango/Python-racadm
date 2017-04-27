#!/usr/bin/python

import os
import commands

f=open("ip.txt","r")
g=open("itag.txt","r")


#ip=f.read().split('\n')
#itag=g.read().split('\n')

#data=dict(zip(ip,itag))


for i in f:
	i=i.strip()

	print "working on",i

	b1=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm get BIOS.Biosbootsettings.bootseq'"%i)
	print b1
	c=b1.split('\n')[1].split('=')[1].split(',')
	print c

	if 'HardDisk.List.1-1' in c:
		c.remove('HardDisk.List.1-1')
		c.insert(0,'HardDisk.List.1-1')
	print c
	order=''
	for nic in c:
		order=order+nic+','

	b2=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm set BIOS.Biosbootsettings.bootseq %s'"%(i,order))	
	print b2
		
	b3=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm jobqueue create BIOS.Setup.1-1'"%i)
	print b3

	b4=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm serveraction hardreset'"%i)
	print b4

	print "============================================================================================="



for i in f:
	i=i.strip()


#Initialise drive
	print "Operating on",i

	s1=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm raid get vdisks'"%i)
	
	print i,s1

	d=s1.split('\n')
	for disk in d:
		s2=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm raid init:%s -speed fast'"%(i,disk))
		print i,':',disk,s2

	s3=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm jobqueue create RAID.Integrated.1-1'"%(i))

	print i,s3

	s4=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm serveraction hardreset'"%(i))

	print i,s4 


	print "============================================================================================================="



#	print "Operating on",i

#       o2 = commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm getversion '" % i)

#	print o2
	
#	if "2.4.2" in o2:
#		continue
#	else:
#        	print i,',',o2





#Delet jobqueue
	print "Operating on",i

        o2 = commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm jobqueue delete --all'" % i)

        print i, o2
        print "=========================================================================================="

	
#Enabling LC controller

	print "Operating on",i

        o2 = commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm set LifecycleController.LCAttributes.LifecycleControllerState 1'" % i)

        print i, o2
        print "=========================================================================================="




#Getting BIOS and Firmware version

	print "Operating on",i

	o2 = commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm getversion -f bios'" % i)

	print i
	print o2
	print "=========================================================================================="


	with open("results.txt","a") as fl:
		fl.write(i+'\n')
		fl.write(o2+'\n')
		fl.write("=================================================")

fl.close()
		

#Power reset

#	print "Operating on",i
#        o1=commands.getoutput("racadm -r %s -u root -p <password> serveraction hardreset"%i)
#        print i,o1

#	try:
#		print "Operating on",i
#		o1=commands.getoutput("racadm -r %s -u root -p <password> serveraction hardreset"%i)
#		print i,o1
#	except:
#	print "Except operation",i
#	o2 = commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm serveraction hardreset'" % i)
#	print i,o2



#Updating ITAg

for i in ip:
	print ('Performing remote IDRAC Operations on -> %s' %i)
	o1 = commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm get iDRAC.NIC.DNSRacName'" %(i))
	print "Current ITAG:",o1

	o2=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm set iDRAC.NIC.DNSRacName %s'" %(i,data[i]))
	print o2
	o3=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm set BIOS.MiscSettings.AssetTag %s'"%(i,data[i]))		
	print o3

	o4 = commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm get iDRAC.NIC.DNSRacName'" % i)
	print o1,o4


	o5=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm jobqueue create BIOS.Setup.1-1'" % i)

	print o5

	o6=commands.getoutput("sshpass -p <password> ssh -o StrictHostKeyChecking=no root@%s 'racadm serveraction hardreset'" % i)

	print o6

	print "===================================================================================================="

	with open("final.txt","a") as f:

		f.write(o1)
		f.write(o2)
		f.write(o3)
		f.write("==============================================")

