import os
import sys
import re
import time
import socket
import colorama

colorama.init()


def print_n_sleep(to_be_printed: str, time_to_sleep: int = 0.3) -> None:
    for meow in to_be_printed.split("\n"):
        print(meow)
        time.sleep(time_to_sleep if meow else 0)


domain_extract_regex_pattern = r"(https://)?([A-Za-z0-9]+(\.[A-Za-z0-9]+)+)/?"

banner = f"""{colorama.Fore.LIGHTRED_EX}
██╗    ██╗██╗  ██╗ ██████╗ ██╗███████╗
██║    ██║██║  ██║██╔═══██╗██║██╔════╝
██║ █╗ ██║███████║██║   ██║██║███████╗
██║███╗██║██╔══██║██║   ██║██║╚════██║
╚███╔███╔╝██║  ██║╚██████╔╝██║███████║
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝

{colorama.Fore.LIGHTGREEN_EX} [1] Start whois
{colorama.Fore.LIGHTYELLOW_EX} [2] Help
{colorama.Fore.LIGHTRED_EX} [3] Exit

{colorama.Fore.LIGHTYELLOW_EX} [+]{colorama.Fore.LIGHTGREEN_EX} Coded by @Tganga36"""

while True:
    os.system("clear")
    print_n_sleep(banner)
    try:
        selected_option = int(input(">>> "))
        match selected_option:
            case 1:
                os.system("clear")
                print_n_sleep("")
                domain = input("Enter domain: ").lower()
                try:
                    base = re.search(domain_extract_regex_pattern, domain)
                    full_domain = base.group(2)
                    ext = base.group(3)

                    if ext in (".com", ".net", ".org"):
                        whois_server = "whois.internic.net"
                    else:
                        whois_server = "whois.iana.org"

                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                        sock.connect((whois_server, 43))
                        sock.send(f"{full_domain}\r\n".encode())
                        whois_result = ""
                        while 1:
                            data = sock.recv(1024)
                            if data:
                                whois_result += data.decode()
                            else:
                                break
                    print_n_sleep(whois_result)

                    if input("Do you want to get whois again? (y/n) ").lower() == "n":
                        break
                    else:
                        continue
                except AttributeError:
                    print("attr error ! (regex)")
            case 2:
                print_n_sleep(
                    f"{colorama.Fore.LIGHTYELLOW_EX}>>> Enter the address of website in domain input."
                )
                if input("Did you understand? (y/n) ").lower() == "n":
                    os.system("clear")
                    print_n_sleep(
                        f"{colorama.Fore.LIGHTYELLOW_EX}>>> Enter the address of website in domain input.",
                        3,
                    )
                continue
            case 3:
                print_n_sleep(f"{colorama.Fore.LIGHTRED_EX}See you later XD")
                break
    except ValueError:
        print("Invalid option !")
