#!/bin/python3
 
import random
import time
import sys

from logo import logo
from password_storage import *

def show_option():
    return r"""
    SYNOPSIS 
        ./main.py [OPTIONS]
    
    DISCRIPTION
        Ne4ecPass is a simple password manager that stores entries as (Name, Password) pairs.
        Data is stored in a basic backend (not encrypted)!
        This project was created by Ne4ec as a hobby. For more info, visit: https://github.com/Ne4ec/Ne4ecPass
        ⚠️ IMPORTANT: Do *not* use this tool to store real passwords.
        It lacks encryption and security measures. Use a trusted, professional password manager instead.
    
    OPTIONS
        -a,    show all stored name and password pairs
        -c,    create a new entry with specified name
        -h,    show this help message and exit
    """

def display_view(content):
    print(40 * '-')
    print(f"{content}")
    print(40 * '-')
    
def password_generator():
    ascii_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!§$@€&/#*<>[]()"
    password = []
    for _ in range(12):
        password.append(random.choice(ascii_characters))
    
    return ''.join(password)

if __name__ == "__main__":

    display_view(logo)
    user_option = sys.argv

    if (len(user_option) != 2):
        print(show_option())
    else:
        if user_option[1] == "-a":
            with open("password_storage.py", 'r') as password_storage_file:
                all_passwords = password_storage_file.read()
                print(all_passwords)
        elif user_option[1] == "-c":
            with open("password_storage.py", 'a') as password_storage_file:
                title_of_new_password = input("What is the title:\n > ").title().strip()
                print(f"You password is creating, for {title_of_new_password} ...")
                generated_password = password_generator()
                time.sleep(0.5)
                password_storage_file.write(f"\nnpm.password['{title_of_new_password}'] = '{generated_password}'")
                display_view(f"Title: {title_of_new_password}\nPassword: {generated_password}")
        elif user_option[1] == "-h":
            print(show_option())
        else:
            print(show_option())
