
import base64
import random
from time import sleep
import re
import time

from pkg.words import words

# defaulte preference
preference_password_length = 15
preference_type = 'random'

class Ne4ecPassManager():
    def __init__(self):
        self.password = {}

    def get_password(self, title):
        if title in self.password:
            time.sleep(0.5)
            return npm.display_view(f"| Title: {title}\n| Password: {npm.base64_decoder(self.password[title])}")
        else:
            return "Sorry, but the password isn't available...\nSee the all password by the name\n - ./main.py -a"

    @staticmethod
    def base64_encoder(string_to_base64):
        string_bytes = string_to_base64.encode("utf-8")
        base64_bytes = base64.b64encode(string_bytes)
        return base64_bytes.decode("ascii")

    @staticmethod
    def base64_decoder(base64_to_string):
        base64_bytes = base64_to_string.encode("ascii")
        string_bytes = base64.b64decode(base64_bytes)
        return string_bytes.decode("utf-8")

    @staticmethod
    def password_generator(password_type, random_password_length=preference_password_length):
        password = []
        if password_type == "random":
            ascii_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!§$@€&/#*<>[]()"
            for _ in range(random_password_length):
                password.append(random.choice(ascii_characters))
            return ''.join(password)

        elif password_type == "memorable":
            for word in words:
                title_word = word.title() + "-"
                password.append(title_word)
            password =  random.sample(password, 5)
            return ''.join(password)[:-1]

    @staticmethod
    def input_validation_number(questions_content, input_len=1, error_content="Please only enter a number!\n"):
        while True:
            user_input_int = input(f"{questions_content}:\n > ")
            try:
                if input_len < len(str(user_input_int)):
                    print(f"Please only length of {input_len}!")
                else:
                    return int(user_input_int)
            except ValueError:
                print(error_content)

    @staticmethod
    def input_validation_string(questions_content):
        while True:
            user_input_string = input(f"{questions_content}:\n > ")
            if re.fullmatch(r"^[a-zA-Z0-9-_ ]+$", user_input_string):
                break
            else:
                print(f"\nUse only following characters\n - a-z\n - A-Z\n - 0-9\n - '_' or '-' \nas input!\nYour input: {user_input_string}\n")
        return user_input_string

    @staticmethod
    def check_backend(title_key):
        if title_key in npm.password:
            print("the title is already used!\nplease use another title...\n" + 40 * '-' + "\n")
        else:
            pass

    @staticmethod
    def display_view(content):
        line = 50
        return line * '-' + f"\n{content}\n" + line * '-'

    @staticmethod
    def successful_commend():
        print("\nGreat, everything is going well.\nFile has been closed.\n")

npm = Ne4ecPassManager()

################### TITLE AND PASSWORDS-###################
