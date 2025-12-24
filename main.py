#!/bin/python3

import random
from time import sleep
import argparse
import base64

from logo import logo
from password_storage import *

def display_view(content):
    return 40 * '-' + f"\n{content}\n" + 40 * '-'
    
def password_generator(length=15): # default value, the user could change it
    ascii_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!§$@€&/#*<>[]()"
    password = []
    for _ in range(length):
        password.append(random.choice(ascii_characters))
    
    return ''.join(password)

def successful_commend():
    print("\nGreat, everything is going well.\nFile has been closed.\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    description =(
        """
        Ne4ecPass is a lightweight, experimental password manager that stores credentials as (Name, Password) pairs. Data is stored using Base64 encoding only and is not encrypted.
        This project was created by Ne4ec as a personal hobby project. For more information, visit the project repository on https://github.com/Ne4ec/Ne4ecPass.
        ⚠ Important: Do not use Ne4ecPass to store real or sensitive passwords. It lacks encryption and essential security protections. For real-world use, rely on a trusted, professional password manager.
            """))

    parser.add_argument("-a", "--all", action="store_true", help="show all Stored name and password pairs")
    parser.add_argument("-c", "--create", action="store_true", help="create a new entry with specified name")
    parser.add_argument("-cp", "--count-password", action="store_true", help="Display the number of passwords stored in the backend")
    parser.add_argument("-g", "--get-a-password", action="store_true", help="show password by the specified name")
    parser.add_argument("-m", "--modify", action="store_true", help="modify the password")

    print(display_view(logo))
    
    args = parser.parse_args()

    if args.all:
        print("Here are all the title and password pairs:\n" + 40 * '-')
        for key, value in npm.password.items():
            print(f"{key}: {npm.base64_decoder(value)}")
        print(40 * '-')
        successful_commend()
    elif args.create:
        with open("password_storage.py", 'a') as backend:
            while True:
                title_of_new_password = input("What is the title:\n > ").title().strip()
                if "'" in title_of_new_password or '"' in title_of_new_password:
                    print("Please, don't the 2 following characters\n - '\n - \"  \nas input!")
                    continue
                elif title_of_new_password in npm.password:
                    print("The title is already used!\nPlease use another title...\n" + 40 * '-' + "\n")
                else:
                    break
            print(f"Your password is creating, for {title_of_new_password}...")
            generated_password = password_generator()
            time.sleep(0.5)
            password_to_base64 = npm.base64_encoder(generated_password)
            backend.write(f"\nnpm.password[str('{title_of_new_password}')] = '{password_to_base64}'") 
            print(display_view(f"| Title: {title_of_new_password}\n| Password: {generated_password} "))
            successful_commend()
    elif args.get_a_password:
        title = input("What is the title of the password you are looking for:\n > ").title().strip()
        npm.get_one_password(title)
        successful_commend()
    elif args.count_password:
        print(f"You have\n > {len(npm.password)} \npasswords stored in the backend.")
        successful_commend()
    elif args.modify:
        with open("password_storage.py", 'a') as password_storage_file:
            while True:
                title_of_modify_password = input("What’s the title of the password you want to modify:\n > ").title().strip()
                if "'" in title_of_modify_password or '"' in title_of_modify_password:
                    print("Please, don't the 2 following characters\n - '\n - \"  \nas input!")
                    continue
                elif title_of_modify_password in npm.password:
                    print(f"Your password is modifing, for {title_of_modify_password}...")
                    modify_generated_password = password_generator()
                    time.sleep(0.5)
                    password_to_base64 = npm.base64_encoder(modify_generated_password)
                    password_storage_file.write(f"\nnpm.password[str('{title_of_modify_password}')] = '{password_to_base64}'")
                    break
                else:
                    print("The password doesn't exit in the backed! \nUse the title which is already saved!\n" + 40 * '-')
            print(display_view(f"| Title: {title_of_modify_password}\n| Password: {modify_generated_password} "))

    else:
        print("./main.py <options>\nUse -h for more help.")
        successful_commend()
