#!/bin/python3
 
import random
from time import sleep
import os
import argparse

from animation import logo
from password_storage import *

def display_view(content):
    print(40 * '-')
    print(f"{content}")
    print(40 * '-')
    
def password_generator(length=15): #*default value, the user could change it
    ascii_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!§$@€&/#*<>[]()"
    password = []
    for _ in range(length):
        password.append(random.choice(ascii_characters))
    
    return ''.join(password)

def successful_commend():
    print("\nGreat, everything is going well.\nFile has been closed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    description =(
        "Ne4ecPass is a simple password manager that stores entries as (Name, Password) pairs. "
        "Data is stored in a basic backend (not encrypted). "
        "This project was created by Ne4ec as a hobby. For more info, visit: https://github.com/ne4ec/PassNe4ec\n\n"
        "⚠️ IMPORTANT: Do *not* use this tool to store real passwords. "
        "It lacks encryption and security measures. Use a trusted, professional password manager instead."))
    
    parser.add_argument("-a", "--all", action="store_true", help="show all Stored name and password pairs")
    parser.add_argument("-c", "--create", action="store_true", help="create a new entry with specified name")
    parser.add_argument("-cp", "--count-password", action="store_true", help="Display the number of passwords stored in the backend")
    parser.add_argument("-g", "--get-a-password", action="store_true", help="show password by the specified name")


    display_view(logo)

    args = parser.parse_args()
    if args.all:
        print("Here are all the title and password pairs:\n" + 40 * '-')
        
        for pair in pm_as_var.password.items():
            print(f"| {pair}")
        print(40 * '-')
        successful_commend()
    elif args.create:
        with open("password_storage.py", 'a') as password_storage_file:
            while True:
                title_of_new_password = input("What is the title:\n > ").title().strip()
                if "'" in title_of_new_password or '"' in title_of_new_password:
                    print("Please, don't the 2 following characters\n - '\n - \"  \nas input!")
                    continue
                elif title_of_new_password in pm_as_var.password:
                    print("The title is already used!\nPlease use another title...\n" + 40 * '-' + "\n")
                else:
                    break
            print(f"You password is creating, for {title_of_new_password}...")
            generated_password = password_generator()
            time.sleep(0.5)
            password_storage_file.write(f"\npm_as_var.password[str('{title_of_new_password}')] = '{generated_password}'")
            display_view(f"| Title: {title_of_new_password}\n| Password: {generated_password} ")
            successful_commend()
    elif args.get_a_password:
        title = input("What is the title of the password you are looking for:\n > ").title().strip()
        pm_as_var.get_one_password(title)
        successful_commend()
    elif args.count_password:
        print(f"You have\n > {len(pm_as_var.password)} \npasswords stored in the backend.")
        successful_commend()
    else:
        print("./main.py <options>\nUse -h for more help.")
        successful_commend()

