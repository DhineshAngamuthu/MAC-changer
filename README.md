# MAC-changer
Powerfull hacking tool to change mac address


# USAGE

git clone https://github.com/DhineshAngamuthu/MAC-changer.git

cd MAC-changer

python3 MAC_changer.py

# Need of changing MAC Address:

    To bypass MAC Address filtering
    To bypass certain kind of MITM spoofing attack
    To avoid device tracking in a public network

There are many other tasks like becoming anonymous in a network and to avoid some network attacks where changing MAC Address becomes useful.


# FAQ
I can see that you are trying the set the Mac address to 11:22:33:44:55:66. And that's the problem. You can only set unicast address and unicast address has to have the first octet as an even value. Try changing the value of the first octet to even (ex: 12:22:33:44:55:66) and it should work.
