#!/bin/python3

import argparse
from time import sleep

from pkg.logo import logo
from pkg.password_storage import *

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
    parser.add_argument("-p", "--preferences", action="store_true", help="set password generation preferences (length, types, visibility)")

    print(npm.display_view(logo))
    
    args = parser.parse_args()

    if args.all:
        print("Here are all the title and password pairs:\n" + 50 * '-')
        for key, value in npm.password.items():
            print( f"| {key}: {npm.base64_decoder(value)}")
        print(50 * '-')
        npm.successful_commend()
    elif args.create:
        while True:
            title_of_new_password = npm.input_validation_string("What is the title")
            if title_of_new_password in npm.password:
                print("The title is already used!\nplease use another title...\n" + 50 * '-' + "\n")
                continue
            else:
                break
        generated_password = npm.password_generator(preference_type, preference_password_length)
        time.sleep(0.5)
        password_to_base64 = npm.base64_encoder(generated_password)
        print(npm.display_view(f"| Title: {title_of_new_password.title()}\n| Password: {generated_password} "))
        with open("pkg/password_storage.py", "a") as backend:
            backend.write(f"\nnpm.password[str('{title_of_new_password}')] = '{password_to_base64}'")
        npm.successful_commend()
    elif args.get_a_password:
        get_tile = npm.input_validation_string("What is the title of the password you are looking for")
        print(npm.get_password(get_tile))
        npm.successful_commend()
    elif args.count_password:
        print(f"You have\n > {len(npm.password)} \npasswords stored in the backend.")
        npm.successful_commend()
    elif args.modify:
        while True:
            title_of_modify_password = npm.input_validation_string("What’s the title of the password you want to modify")
            if title_of_modify_password not in npm.password:
                print("The password doesn't exit in the backed!\nUse the title which is already saved!\n" + 40 * '-')
                continue
            else:
                with open("pkg/password_storage.py", 'a') as password_storage_file:
                    print(f"Your password is modifing, for {title_of_modify_password}...")
                    modify_generated_password = npm.password_generator(preference_type)
                    time.sleep(0.5)
                    password_to_base64 = npm.base64_encoder(modify_generated_password)
                    password_storage_file.write(f"\nnpm.password[str('{title_of_modify_password}')] = '{password_to_base64}'")
                    print(npm.display_view(f"| Title: {title_of_modify_password}\n| Password: {modify_generated_password} "))

                    password_to_base64 = npm.base64_encoder(modify_generated_password)
                    password_storage_file.write(f"\nnpm.password[str('{title_of_modify_password}')] = '{password_to_base64}'")
                    break
        npm.successful_commend()
    elif args.preferences:
        print(f"What you want to change?\n - (1) Password-lentgh (current: {preference_password_length})\n - (2) Password-type (current: {preference_type})\n" + 50 * '-')
        preference_selection = npm.input_validation_number("Select one of the numbers (1/2)")
        with open("pkg/password_storage.py", 'a') as preference_backend:
            if preference_selection == 1:
                new_password_length = npm.input_validation_number("What password length do you want (default=15)", 2, error_content="Can have up to 99 digits!")
                preference_backend.write(f"\npreference_password_length = {new_password_length}")
            elif preference_selection == 2:
                print("You can choose between (default=random)\n - (1) random characters (e.g: 4?nlS4)\n - (2) memorable words (e.g: Dog-Computer)\n" + 50 * '-')
                new_password_type = npm.input_validation_number("Select one of numbers(1/2)")
                password_type = {1: "random", 2: "memorable"}
                preference_backend.write(f"\npreference_type = '{password_type[new_password_type]}'")
        npm.successful_commend()
    else:
        print("./main.py <options>\nUse -h for more help.")
        npm.successful_commend()
