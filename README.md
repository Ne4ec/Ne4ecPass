# Ne4ecPass version 0.4 
![creation_of_a_password_poc](https://github.com/Ne4ec/Ne4ecPass/blob/main/pkg/.pictures/poc.png)<br>
A CLI password manager, created with Python. It is for educational purposes only - do not use it as your default password manager! 
____
## Installation
### Linux
1. Before we begin, we need to install Python to execute the program, as well as Git to install the repository
```bash
sudo pacman -Syu python git 
```
**Notice:** If you're using a different Linux distribution (`apt` or `dnf` etc.), make sure to use the correct `package manager`. The steps should be similar across distributions. <br>
2. after that, install my repository
```bash
git clone https://github.com/Ne4ec/Ne4ecPass
cd Ne4ecPass
```
3. Now we are finished, its upon on you, what do you want to do. See the usage
### Windows
1. First, you need to install the following tools
- git: [GIT for Windows](https://git-scm.com/downloads/win)
- python: [Python for Windows](https://www.python.org/downloads/windows/)

Make sure to download the version that matches your system architecture — most commonly 64-bit. Run the Git installer to complete the setup. If you run into any issues during installation, refer to these guides
- for git [Getting Started - Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- for python [Downloading Python](https://wiki.python.org/moin/BeginnersGuide/Download)

After installation, open the folder where the Git executable was downloaded (typically your `Downloads` folder). In the File Explorer’s address bar, type `cmd.exe` and press Enter. This will open a terminal window in that directory.

2. write here the following commend
```bash
git clone https://github.com/Ne4ec/Ne4ecPass
cd Ne4ecPass
```
3. Now you are finished. Go now the the Usage of the password manager.
____
## Usage
A simple password manager that allows you to create a password and assign it a name.
```
usage: main.py [-h] [-a] [-c] [-cp] [-g] [-m] [-p]

Ne4ecPass is a lightweight, experimental password manager that stores credentials as (Name, Password) pairs. Data is
stored using Base64 encoding only and is not encrypted. This project was created by Ne4ec as a personal hobby
project. For more information, visit the project repository on https://github.com/Ne4ec/Ne4ecPass. ⚠ Important: Do
not use Ne4ecPass to store real or sensitive passwords. It lacks encryption and essential security protections. For
real-world use, rely on a trusted, professional password manager.

options:
  -h, --help            show this help message and exit
  -a, --all             show all Stored name and password pairs
  -c, --create          create a new entry with specified name
  -cp, --count-password
                        Display the number of passwords stored in the backend
  -g, --get-a-password  show password by the specified name
  -m, --modify          modify the password
  -p, --preferences     set password generation preferences (length, types, visibility)
```
**Warning**: This project is designed for learning purposes only. It is not intended for professional use and is suitable for school or study projects.
____
## Conculution
Hopefully, everything is working. If not, please leave a comment in the Issues tab. Thank you for paying attention, and have a nice day :)<br>
~ Ne4ec
___
