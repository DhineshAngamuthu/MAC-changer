import subprocess
import re

#call() and check_output() are important process - re = regex

interface = input("Enter Interface Name: ")
new_mac = input("Enter New MAC: ")

# ifconfig eth0 down
subprocess.call(["ifconfig",interface,"down"])
#ifconfig eth0 hw ether<MAC address>
subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
#ifconfig eth0 up
subprocess.call(["ifconfig",interface,"up"])

#output
output = str(subprocess.check_output(["ifconfig",interface]))

#r to make readable
changed_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",output)

#check
if new_mac == changed_mac.group(0):
  print("MAC Address changed Succesfully..!!!")
