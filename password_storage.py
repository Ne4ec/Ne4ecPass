import time
import base64

def display_get_one_password(title, passsword):
    return 40 * '-' + f"\n| Title: {title}\n| Password: {npm.base64_decoder(passsword)}\n" + 40 * '-'

class Ne4ecPassManager():
    def __init__(self):
        self.password = {}

    def get_one_password(self, title):
        if title in self.password:
            time.sleep(0.5)
            print(display_get_one_password(title, self.password[title]))
        else:
            print("Sorry, but the password isn't available...\nSee the all password by the name\n - ./main.py -a")

    def base64_encoder(self, string_to_base64):
        string_bytes = string_to_base64.encode("utf-8")
        base64_bytes = base64.b64encode(string_bytes)
        return base64_bytes.decode("ascii")

    def base64_decoder(self, base64_to_string):
        base64_bytes = base64_to_string.encode("ascii")
        string_bytes = base64.b64decode(base64_bytes)
        return string_bytes.decode("utf-8")


npm = Ne4ecPassManager()

################### TITLE AND PASSWORDS-###################
