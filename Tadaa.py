/usr/bin/python

###################################

#A simple local TCP port scanner for Linux
#author:Hadi Tux

# Usage

#./Tadaa.py 
# default ports

#./Tadaa.py --port=22 
# check if port 22 is open

#./Tadaa.py --port=22,80,443
# check if ports 20,80,443 are open

#./Tadaa.py --port=1-65500
# scan all ports between 1 and 65000

##################################
import commands
import optparse
import sys

if sys.platform.startswith("linux"):
	pass
else:
	sys.exit("[-]Tadaa is only for Linux platform")

menu = """

___________           .___              
\__    ___/____     __| _/____  _____   
  |    |  \__  \   / __ |\__  \ \__  \  
  |    |   / __ \_/ /_/ | / __ \_/ __ \_
  |____|  (____  /\____ |(____  (____  /
               \/      \/     \/     \/ 

               		A simple local TCP port scanner for Linux
               		Hadi Tux
               		@Suspicious Shell Activity

"""

parser = optparse.OptionParser()
parser.add_option("--port","-p",help="ports to scan ",dest="port")
opt , args = parser.parse_args()

print(menu)

if not opt.port :
	print("[*]Scanning default ports  ... for others ports use --port options")
	for tcp in range(1,2001):
		Output = commands.getoutput("netstat -an | grep '\\b{}\\b' | grep LISTEN | grep tcp".format(str(tcp)))
		if str((tcp)) in (Output):
			print("[+]Port {} is Open".format(str(tcp)))
		elif not str((tcp)) in (Output):
			pass

elif opt.port and "," in (opt.port) :
	for tcp in (opt.port).split(","):
		Output = commands.getoutput("netstat -an | grep '\\b{}\\b' | grep LISTEN | grep tcp".format(str(tcp)))
		if str((tcp)) in (Output):
			print("[+]Port {} is Open".format(str(tcp)))
		elif not str((tcp)) in (Output):
			print("[-]Port {} is Closed".format(str(tcp)))	

elif opt.port and "-" in (opt.port) :
	lol = (opt.port).split("-")

	for tcp in range(int(lol[0]),int(lol[1])+1):

		Output = commands.getoutput("netstat -an | grep '\\b{}\\b' | grep LISTEN | grep tcp".format(str(tcp)))
		if str((tcp)) in (Output):
			print("[+]Port {} is Open".format(str(tcp)))	
		elif not str((tcp)) in (Output):
			pass
else:
	Output = commands.getoutput("netstat -an | grep '\\b{}\\b' | grep LISTEN | grep tcp".format(str(opt.port)))
	if opt.port in (Output):
		print("[+]Port {} is Open".format(str(opt.port)))	
	elif not opt.port in (Output):
		print("[-]Port {} is Closed".format(str(opt.port)))


print("[*]Scan Finished")
