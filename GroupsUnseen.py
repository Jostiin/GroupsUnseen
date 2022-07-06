
import os
from GU import *
import webbrowser
import time
from colorama import init, Fore

init(convert=True)
def Menu_Principal():
    while True:
        os.system('cls')
        ad = ''.join(database.select_ads())
        print(Fore.RED+'''
     ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗ ███████╗'''+Fore.BLUE+'''██╗   ██╗███╗   ██╗███████╗███████╗███████╗███╗   ██╗'''+Fore.RED+'''
    ██╔════╝ ██╔══██╗██╔═══██╗██║   ██║██╔══██╗██╔════'''+Fore.BLUE+''' ██║   ██║████╗  ██║██╔════╝██╔════╝██╔════╝████╗  ██║'''+Fore.RED+'''
    ██║  ███╗██████╔╝██║   ██║██║   ██║██████╔╝███████╗'''+Fore.BLUE+'''██║   ██║██╔██╗ ██║███████╗█████╗  █████╗  ██╔██╗ ██║'''+Fore.RED+'''
    ██║   ██║██╔══██╗██║   ██║██║   ██║██╔═══╝ ╚════██║'''+Fore.BLUE+'''██║   ██║██║╚██╗██║╚════██║██╔══╝  ██╔══╝  ██║╚██╗██║'''+Fore.RED+'''
    ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║     ███████║'''+Fore.BLUE+'''╚██████╔╝██║ ╚████║███████║███████╗███████╗██║ ╚████║'''+Fore.RED+'''
    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝ '''+Fore.BLUE+'''╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝
                                        Create by: Jostin Orbe    

        '''+Fore.RED+'''[Ads]'''+Fore.WHITE+''': '''+Fore.BLUE+ad+'''    

        ['''+Fore.RED+'''1'''+Fore.BLUE+''']'''+Fore.GREEN+''' WhatsApp'''+Fore.BLUE+'''
        ['''+Fore.RED+'''2'''+Fore.BLUE+''']'''+Fore.BLUE+''' Telegram
        ['''+Fore.RED+'''3'''+Fore.BLUE+'''] '''+Fore.YELLOW+'''Login'''+Fore.YELLOW+'''['''+Fore.RED+'''Admins'''+Fore.YELLOW+''']'''+Fore.BLUE+'''
        ['''+Fore.RED+'''4'''+Fore.BLUE+''']'''+Fore.RED+''' Quit                                                                                                                                                                                                                         
                                                                                                            '''+Fore.WHITE)
        try:
            ChooseOption = int(input("        : Opcion : "))
            if ChooseOption == 1:
                Menu_WhatsApp()
            elif ChooseOption == 2:
                Menu_Telegram()
            elif ChooseOption == 3:
                Login_Admins()
            elif ChooseOption == 4:
                os.system('cls')
                print(Fore.GREEN+'Gracias por utilizar GroupUnseen :)'+Fore.RESET)
                break
            else:
                pass
        except ValueError:
            print('error')



def Menu_WhatsApp():
    while True:
        os.system('cls')
        print(Fore.RED+'|'+Fore.GREEN+' WHATSAPP GROUPS '+Fore.RED+'|'+Fore.RED+'\n------------------------------\n'+Fore.RESET)
        database.select_group_All('groupswhatsapp')
        print(Fore.BLUE+'['+Fore.RED+'200'+Fore.BLUE+']'+Fore.BLUE+' Search'+Fore.RESET)
        print(Fore.BLUE+'['+Fore.RED+'100'+Fore.BLUE+']'+Fore.WHITE+' Back\n'+Fore.RESET)
        try:
            ChooseOptionW = int(input(': Opcion : '))
            if ChooseOptionW == 100:
                Menu_Principal()
            elif ChooseOptionW == 200:
                os.system('cls')
                print(Fore.BLUE)
                search = str(input('Search: '))
                print(Fore.RESET)
                database.search_groups(search,'groupswhatsapp')
                print(Fore.BLUE+'['+Fore.RED+'100'+Fore.BLUE+']'+Fore.WHITE+' Back\n'+Fore.RESET)
                try:
                    ChooseOption = int(input(': Opcion : '))
                    if ChooseOption == 100:
                        break
                    else:
                        while True:
                            os.system('cls')
                            print(Fore.RED)
                            database.select_group_One('groupswhatsapp',ChooseOptionW)
                            
                            try:
                                ChooseOptionW2 = int(input(': Opcion : '))
                                if ChooseOptionW2 == 100:
                                    print(Fore.BLUE+'Opening URL...')
                                    time.sleep(5)
                                    webbrowser.open(str(database.select_URL('groupswhatsapp',ChooseOptionW)))
                                    print(Fore.GREEN+'URL open successfully')
                                    database.Add_United('groupswhatsapp',ChooseOptionW)
                                    time.sleep(5)
                                elif ChooseOptionW2 == 300:
                                    os.system('cls')
                                    database.Add_Stars('groupswhatsapp',ChooseOptionW)
                                    print(Fore.YELLOW+'You have given a star'+Fore.RESET)
                                    time.sleep(5)
                                else:
                                    break
                            except ValueError:
                                print('error')
                except:
                    pass
            else:
                while True:
                    os.system('cls')
                    print(Fore.RED)
                    database.select_group_One('groupswhatsapp',ChooseOptionW)
                    try:
                        ChooseOptionW2 = int(input(': Opcion : '))
                        if ChooseOptionW2 == 100:
                            print(Fore.BLUE+'Opening URL...')
                            time.sleep(5)
                            webbrowser.open(str(database.select_URL('groupswhatsapp',ChooseOptionW)))
                            print(Fore.GREEN+'URL open successfully')
                            database.Add_United('groupswhatsapp',ChooseOptionW)
                            time.sleep(5)
                        elif ChooseOptionW2 == 300:
                            os.system('cls')
                            database.Add_Stars('groupswhatsapp',ChooseOptionW)
                            print(Fore.YELLOW+'You have given a star'+Fore.RESET)
                            time.sleep(5)
                        else:
                            break
                    except ValueError:
                        print('error')
            
        except ValueError:
            print('error')
        
def Menu_Telegram():
    while True:
        os.system('cls')
        print(Fore.RED+'|'+Fore.BLUE+' TELEGRAM GROUPS '+Fore.RED+'|'+Fore.RED+'\n------------------------------\n'+Fore.RESET)
        database.select_group_All('groupstelegram')
        print(Fore.BLUE+'['+Fore.RED+'200'+Fore.BLUE+']'+Fore.BLUE+' Search'+Fore.RESET)
        print(Fore.BLUE+'['+Fore.RED+'100'+Fore.BLUE+']'+Fore.RED+' Back\n'+Fore.WHITE)
        try:
            ChooseOptionW = int(input(': Opcion : '))
            if ChooseOptionW == 100:
                Menu_Principal()
            elif ChooseOptionW == 200:
                os.system('cls')
                print(Fore.BLUE)
                search = str(input('Search: '))
                print(Fore.RESET)
                database.search_groups(search,'groupswhatsapp')
                print(Fore.BLUE+'['+Fore.RED+'100'+Fore.BLUE+']'+Fore.WHITE+' Back\n'+Fore.RESET)
                try:
                    ChooseOption = int(input(': Opcion : '))
                    if ChooseOption == 100:
                        break
                    else:
                        while True:
                            os.system('cls')
                            print(Fore.RED)
                            database.select_group_One('groupswhatsapp',ChooseOptionW)
                            
                            try:
                                ChooseOptionW2 = int(input(': Opcion : '))
                                if ChooseOptionW2 == 100:
                                    print(Fore.BLUE+'Opening URL...')
                                    time.sleep(5)
                                    webbrowser.open(str(database.select_URL('groupswhatsapp',ChooseOptionW)))
                                    print(Fore.GREEN+'URL open successfully')
                                    database.Add_United('groupswhatsapp',ChooseOptionW)
                                    time.sleep(5)
                                elif ChooseOptionW2 == 300:
                                    os.system('cls')
                                    database.Add_Stars('groupswhatsapp',ChooseOptionW)
                                    print(Fore.YELLOW+'You have given a star'+Fore.RESET)
                                    time.sleep(5)
                                else:
                                    break
                            except ValueError:
                                print('error')
                except:
                    pass
            else:
                while True:
                    os.system('cls')
                    database.select_group_One('groupstelegram',ChooseOptionW)
                    try:
                        ChooseOptionW2 = int(input(': Opcion : '))
                        if ChooseOptionW2 == 100:
                            print(Fore.BLUE+'Opening URL...')
                            time.sleep(5)
                            webbrowser.open(str(database.select_URL('groupstelegram',ChooseOptionW)))
                            print(Fore.GREEN+'URL open successfully') 
                            database.Add_United('groupstelegram',ChooseOptionW)       
                            time.sleep(5)
                        elif ChooseOptionW2 == 300:
                            os.system('cls')
                            database.Add_Stars('groupstelegram',ChooseOptionW)
                            print(Fore.YELLOW+'You have given a star',Fore.RESET) 
                            time.sleep(5)
                        else:
                            break
                    except ValueError:
                        print('error')
        except ValueError:
            print('error')

def Login_Admins():
    while True:
        os.system('cls')
        print(Fore.BLUE+'Login Admin'+Fore.WHITE)
        username = str(input('Username: '))
        Password = str(input('Password: '))
        if database.select_Admins('Admins',username,Password) == True:
            while True:
                os.system('cls')
                print(Fore.BLUE+'MENU ADMIN')
                print(Fore.BLUE+'['+Fore.RED+'1'+Fore.BLUE+']'+Fore.WHITE+'Insert group')
                print(Fore.BLUE+'['+Fore.RED+'2'+Fore.BLUE+']'+Fore.WHITE+'Ads')
                print(Fore.BLUE+'['+Fore.RED+'100'+Fore.BLUE+']'+Fore.RED+'Back')
                ChooseOption = int(input(': Opcion : '))
                if ChooseOption == 1:
                    while True:
                        os.system('cls')
                        print(Fore.BLUE+'INSERT GROUP')
                        print(Fore.BLUE+'['+Fore.RED+'1'+Fore.BLUE+']'+Fore.GREEN+' WhatsApp\n'+Fore.BLUE+'['+Fore.RED+'2'+Fore.BLUE+']'+Fore.BLUE+' Telegram\n'+Fore.BLUE+'['+Fore.RED+'100'+Fore.BLUE+']'+Fore.RED+' Back'+Fore.WHITE)
                        ChooseOption = int(input(': Option : '))
                        if ChooseOption == 1:
                            while True:
                                os.system('cls')
                                print(Fore.RED+'|'+Fore.GREEN+' INSERT WHATSAPP GROUPS '+Fore.RED+'|'+Fore.RESET)
                                Group_Name = str(input('\nGroup Name: '))
                                Group_Review = str(input('Group Review: '))
                                Group_URL = str(input('\nGroup URL: '))
                                database.Insert_Group('groupswhatsapp',str(Group_Name),str(Group_URL),str(Group_Review),int(0))
                                time.sleep(10)
                                break
                        elif ChooseOption == 2:
                            while True:
                                os.system('cls')
                                print(Fore.RED+'|'+Fore.GREEN+' INSERT TELEGRAM GROUPS '+Fore.RED+'|'+Fore.RESET)
                                Group_Name = str(input('\nGroup Name: '))
                                Group_Review = str(input('Group Review: '))
                                Group_URL = str(input('\nGroup URL: '))
                                database.Insert_Group('groupstelegram',str(Group_Name),str(Group_URL),str(Group_Review),int(0))
                                time.sleep(10)
                                break
                        elif ChooseOption == 100:
                            Menu_Principal()
                        else:
                            pass
                elif ChooseOption == 2:
                    os.system('cls')
                    print(Fore.BLUE+'INSERT AD'+Fore.WHITE)
                    anuncio = str(input('Ad: '))
                    database.insert_ads(anuncio)
                    time.sleep(5)
                elif ChooseOption == 3:
                    break
                else:
                    continue

        else:     
            print(Fore.RED+'Incorrect password'+Fore.RESET)
            time.sleep(5)

Menu_Principal()