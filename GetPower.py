#!/usr/bin/python

import paramiko
import sys

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Name a file with IP's as 1st argument
fip = open(sys.argv[1], 'r')

#Second argument is username
uname = sys.argv[2]

#Third argument is password
pwrd = sys.argv[3]

for line in fip.readlines():
	try :
		ssh.connect(line, username=uname, password=pwrd)

	except paramiko.AuthenticationException:

		print '[-] Username %s and %s pass are Bad!' % (uname,pwrd)

	else :
		(stdin, stdout, stderr) = ssh.exec_command('show power inline')

		for pline in stdout.readlines():
			print pline
		ssh.close()

