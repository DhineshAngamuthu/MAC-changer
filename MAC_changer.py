import subprocess
import re

#call() and check_output() are important process - re = regex

interface = input("Enter interface name: ")
new_mac = input("Enter new MAC: ")

# ifconfig eth0 down
subprocess.call(["ifconfig",interface,"down"])
#ifconfig eth0 hw ether<MAC address>
subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
#ifconfig eth0 up
subprocess.call(["ifconfig",interface,"up"])

