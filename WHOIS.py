import socket
from colorama import Fore
import os
import sys
import time
import colorama
def whois():
    colorama.init()
    os.system("clear")
    print("")
    print( Fore.LIGHTRED_EX + """██╗    ██╗██╗  ██╗ ██████╗ ██╗███████╗
██║    ██║██║  ██║██╔═══██╗██║██╔════╝
██║ █╗ ██║███████║██║   ██║██║███████╗
██║███╗██║██╔══██║██║   ██║██║╚════██║
╚███╔███╔╝██║  ██║╚██████╔╝██║███████║
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝
                                      """)
    print("")
    time.sleep(0.3)
    print(Fore.LIGHTGREEN_EX + "[1] WHOIS start...")
    print("")
    time.sleep(0.3)
    print(Fore.LIGHTYELLOW_EX + "[2] help...")
    print("")
    time.sleep(0.3)
    print(Fore.LIGHTRED_EX + "[3] Exit...")
    print("")
    print(Fore.LIGHTYELLOW_EX + "[+]" + Fore.LIGHTGREEN_EX + "create by @Tganga36")
    print("")
    x = input(">>> ")
    #----------------------------------------

    if x == "1":
        os.system("clear")
        print("")
        time.sleep(0.3)
        domain = input("Domain : ").lower()

        domain = domain.replace("http://","")
        domain = domain.replace("https://","")
        domain = domain.replace("www.","")

        if domain[-3:] == "org" or domain[-3:] == "com" or domain[-3:] == "net":
            whois_server = "whois.internic.net"
        else:
            whois_server =  "whois.iana.org"

        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

        s.connect((whois_server,43))

        s.send((domain+"\r\n").encode())

        msg = s.recv(10000)

        print(msg.decode())
        we = input("again :")
        if we == "yes" :
            whois()
        else :
            os.system("clear")
    
#............................................

    if x == "2":
        print(Fore.LIGHTYELLOW_EX + """ >>> In the domain field, enter the address of your desired site .... """)
        print("")
        qw = input( " Did you understand ? ")
        if qw == "yes":
            whois()
        else :
            print("")
            print(Fore.LIGHTYELLOW_EX + """ >>> In the domain field, enter the address of your desired site .... """)
            time.sleep(5)
            whois()
    if x == "3":
        if x == "3":
            print( Fore.LIGHTRED_EX + "see you Later ;) ")
            time.sleep(0.2)
            



whois()
    
