# here are all the password, which is created by the password generator

import time

def display_get_one_password(title, passsword):
    print(40 * '-')
    print(f"Title: {title}")
    print(f"Password: {passsword}")
    print(40 * '-')

class Ne4ecPassManager():
    def __init__(self):
        self.password = {}
    
npm = Ne4ecPassManager()

################### TITLE AND PASSWORDS-###################
# Name | Password
