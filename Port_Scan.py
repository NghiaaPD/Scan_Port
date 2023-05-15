#Use these commands in Kali to install required software:
#  sudo apt install python3-pip
#  pip install python-nmap


import nmap

import re

# Regular Expression Pattern to recognise IPv4 addresses.
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")


port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

port_min = 0
port_max = 65535

# This port scanner uses the Python nmap module.
# You'll need to install the following to get it work on Linux:
# Step 1: sudo apt install python3-pip
# Step 2: pip install python-nmap



print(r"""
______  ____           ____                  ______   _______
|     \ |  |           |  |                  |  _  \  |  _   \
|      \|  |  ______   |  |        ___ ___   | |_)  | |  |\   \
|   |\     | / ____ \  |  | _____  | | _` \  |   __/  |  | )   |
|   | |    || (____) | |  |/ __  \ | | (_| | |   |    |  |/   /
|___| |____| \____  /  |____/  \__\|_|\__,_| |___|    |______/
                  | |   
                  | |                               
              ____| |
              \_____/                                               """)

print("\n********************************************************************************************************************************")
print("* cíu bé nghĩa ssl                                                                                                             *")
print("* https://phanducnghianpd-8fctfdchp-nghiaapd.vercel.app/?fbclid=IwAR2kdoZw_hDW8UL62BgUYRvBAJkBSA0sb60-G6eAx2IaO0pvOkktd2UKbO4  *")
print("* https://www.facebook.com/nghiapd1/                                                                                           *")
print("********************************************************************************************************************************")

open_ports = []
# Ask user to input the ip address they want to scan.
while True:
    ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} is a valid ip address")
        break

while True:

    # all the ports is not advised.
    print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

nm = nmap.PortScanner()

for port in range(port_min, port_max + 1):
    try:

        # For in nmap for port 80 and ip 10.0.0.2 you'd run: nmap -oX - -p 89 -sV 10.0.0.2
        result = nm.scan(ip_add_entered, str(port))

        # We extract the port status from the returned object
        port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
        print(f"Port {port} is {port_status}")
    except:
        # We cannot scan some ports and this ensures the program doesn't crash when we try to scan them.
        print(f"Cannot scan port {port}.")
