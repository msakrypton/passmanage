from banner import *
import sys
from colorama import Fore


#------------HOME-MENU------------#

def home():
    banner_manege()

    print(Fore.WHITE+"[1] Accounts Password\n")
    print(Fore.WHITE+"[2] Password Generator\n") 
    print(Fore.WHITE+"[3] Exit :)\n")

#---------------ACCOUNTSPASS---------------#

def accounts_pass():
    banner_accounts()

    print(Fore.WHITE+"[1] Init a Table\n")
    print(Fore.WHITE+"[2] Add Password Account\n")
    print(Fore.WHITE+"[3] Show Accounts Password\n")
    print(Fore.WHITE+"[4] Back To Home :)\n")

#---------------ADD-ACCOUNTS-------------#

def add_account():
    banner_accounts()

    print(Fore.WHITE+'[1] Instagram\n')
    print(Fore.WHITE+'[2] Facebook\n')
    print(Fore.WHITE+'[3] Gmail\n')
    print(Fore.WHITE+'[4] Yahoo\n')
    print(Fore.WHITE+'[5] Other Apps\n')
    print(Fore.WHITE+'[6] Other Websites\n')
    print(Fore.WHITE+'[7] Devices')

#-----------------PASSGEN----------------#

def passgen():
    banner_gen()
    import random

    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$&*_'

    try:
        length = int(input(Fore.WHITE+"[*] Length Pass: "))
        print('')
        num_of_pass = int(input(Fore.WHITE+"[*] Number Of Pass: "))
        print('')
    
        for p in range(num_of_pass):
            list_pass = []
            password = ''
            for c in range(length):
                password += random.choice(chars)
            list_pass.append(password)
            str_pass = ''.join(list_pass)

            print(Fore.WHITE+str_pass)

        print(Fore.GREEN+'''\nUse these strong passwords to register on social networks and site!''')
    
    except ValueError:
        passgen()

    again = input(Fore.BLUE+'\nAgain? [Y/n] ')
    if again == 'y' or again == 'Y':
        passgen()
    elif again == 'n' or again == 'N':
        backtohome()
    else:
        backtohome()

#---------------------BACK-TO-HOME---------------------#

def backtohome():
    try:
        ret_home = input(Fore.WHITE+'\nBack To Home? [Y/n] ')
        if ret_home == 'y' or ret_home == 'Y':
            home()
        elif ret_home == 'n' or ret_home == 'N':
            print('\nGood Bye!')
            sys.exit()
        else:
            sys.exit()
    except:
        print('')
        sys.exit()    

#------------------------------------------------------#
