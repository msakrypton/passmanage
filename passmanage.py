from api import *
from banner import *
from menus import *
from tabulate import tabulate
from colorama import Fore
import sys
import os 


home()

while True:

    try:

        home_input = int(input(Fore.GREEN+'Home'+Fore.WHITE+':'+Fore.LIGHTBLUE_EX+'~'+Fore.WHITE+'$ '))
        if home_input != 1 or home_input != 2 or home_input != 3:
            os.system('clear')
            home()

    except:
        os.system('clear')
        home()

#------------------ACCOUNTS-PASS-------------------#    
    
    if home_input == 1:
        accounts_pass()

        account_input = int(input(Fore.LIGHTRED_EX+'AccountsPass'+Fore.WHITE+':'+Fore.LIGHTBLUE_EX+'~'+Fore.WHITE+'$ '))
                
    #--------------INIT--------------#      
        
        if account_input == 1:
            init()
            print(Fore.GREEN+'\ntable was created!\n')
            break

    #------------ADD-------------#    

        elif account_input == 2:
            add_account()
            topic = int(input(Fore.WHITE+'\n[*] Enter number of topic: '))

            if topic == 1:
                username = input('[*] Enter Username: ')
                password = input('[*] Enter Password: ')
                add('Instagram', username, password)

            elif topic == 2:
                username = input('[*] Enter UserName: ')
                password = input('[*] Enter Password: ')
                add('Facebook', username, password)

            elif topic == 3:
                email = input('[*] Enter Email: ')
                password = input('[*] Enter Password: ')
                add('Gmail', email, password)

            elif topic == 4:
                email = input('[*] Enter Email: ')
                password = input('[*] Enter Password: ')
                add('Yahoo', email, password)

            elif topic == 5:
                app_name = input('[*] Name of app: ')
                password = input('[*] Enter Password: ')
                add('App', app_name, password)

            elif topic == 6:
                web_name = input('[*] Name of website: ')
                password = input('[*] Enter Password: ')
                add('Website', web_name, password)

            elif topic == 7:
                device = input('[*] Device Name: ')
                password = input('[*] Enter Password: ')
                add('Device', device, password)

            print(Fore.GREEN+'\nYour account has been added!')
            print('')
            break

    #---------------SHOW---------------#    
                                    
        elif account_input == 3:
            banner_accounts()

            print(Fore.WHITE+"[1] Show All\n")
            print(Fore.WHITE+"[2] View ‌By Topic\n")
            
            show_data = int(input(Fore.LIGHTRED_EX+'AccountsPass'+Fore.WHITE+':'+Fore.LIGHTBLUE_EX+'~'+Fore.WHITE+'$ '))

            if show_data == 1:
                print('')
                print(tabulate(show()))
                backtohome()
            try:
                if show_data == 2:
                    add_account()
                    topic = int(input('\n[*] Enter Topic: '))
                    if topic == 1:
                        results = show('Instagram')
                    elif topic == 2:
                        results = show('Facebook')
                    elif topic == 3:
                        results = show('Gmail')
                    elif topic == 4:
                        results = show('Yahoo')
                    elif topic == 5:
                        results = show('App')
                    elif topic == 6:
                        results = show('Website')
                    elif topic == 6:
                        results = show('Device')

                    print('')
                    print(tabulate(results))
                    backtohome()
            except NameError:
                print('Error')
    #-----------BACK-------------#  
        
        elif account_input == 4:
            home()
        
        else:
            os.system('clear')
            accounts_pass()

#---------------PASS-GEN---------------#
        
    if home_input == 2:
        passgen()

#-----------------EXIT----------------#

    if home_input == 3:
        print('Good bye!!\n')
        break

