# here are all the password, which is created by the password generator

import time

def display_get_one_password(title, passsword):
    #print(40 * '-')
    return 40 * '-' + f"\n| Title: {title}\n| Password: {passsword}\n" + 40 * '-'

class Ne4ecPassManager():
    def __init__(self):
        self.password = {}
    
    def get_one_password(self, title):
        if title in self.password:
            time.sleep(0.5)
            print(display_get_one_password(title, self.password[title]))
            #display_get_one_password
        else:
            print("Sorry, but the password isn't available...\nSee the all password by the name\n - ./main.py -a")

pm_as_var = Ne4ecPassManager()

################### TITLE AND PASSWORDS-###################
# Name | Password
