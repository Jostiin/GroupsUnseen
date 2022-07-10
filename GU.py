from pymongo import MongoClient
from colorama import init, Fore
from pyfiglet import Figlet
import smtplib, ssl, datetime

init(convert=True)
#----------------------------MYSQL-----------------------------------
class DataBase:

    def __init__(self):
        self.client = MongoClient('mongodb://uu762vs76lwyz0bxulaf:FajtTFXylgwALp5BdE4R@n1-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017,n2-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017/bjzbcdi3vegpr9k?replicaSet=rs0')
        self.db = self.client.bjzbcdi3vegpr9k 

    def select_group_One(self,bd,ID):
        if bd == 'GroupsWhatsApp':
            BDGroupsW = self.db.GroupsWhatsApp.find_one({"ID":ID})
            custom_fig = Figlet(font=str('standard'))
            print(custom_fig.renderText(f'{BDGroupsW["NAME"]}'))
            print(f'{Fore.BLUE}{BDGroupsW["DESCRIPTION"]}\n\nURL{Fore.WHITE}:{Fore.GREEN} {BDGroupsW["URL"]}\n')
            print(f'{Fore.YELLOW}({BDGroupsW["STARS"]})Stars\n')
            print(f'{Fore.WHITE}{BDGroupsW["PEOPLE_JOIN"]} people have joined\n')
            print(f'{Fore.BLUE}[{Fore.RED}100{Fore.BLUE}] {Fore.GREEN}Join Group')
            print(f'{Fore.BLUE}[{Fore.RED}300{Fore.BLUE}] {Fore.YELLOW}Qualify')
            print(f'{Fore.BLUE}[{Fore.RED}200{Fore.BLUE}] {Fore.RED}Back{Fore.WHITE}\n')
        elif  bd == 'GroupsTelegram':
            BDGroupsT = self.db.GroupsTelegram.find_one({"ID":ID})
            custom_fig = Figlet(font=str('standard'))
            print(custom_fig.renderText(f'{BDGroupsT["NAME"]}'))
            print(f'{Fore.BLUE}{BDGroupsT["DESCRIPTION"]}\n\nURL{Fore.WHITE}:{Fore.GREEN} {BDGroupsT["URL"]}\n')
            print(f'{Fore.YELLOW}({BDGroupsT["STARS"]})Stars\n')
            print(f'{Fore.WHITE}{BDGroupsT["PEOPLE_JOIN"]} people have joined\n')
            print(f'{Fore.BLUE}[{Fore.RED}100{Fore.BLUE}] {Fore.GREEN}Join Group')
            print(f'{Fore.BLUE}[{Fore.RED}300{Fore.BLUE}] {Fore.YELLOW}Qualify')
            print(f'{Fore.BLUE}[{Fore.RED}200{Fore.BLUE}] {Fore.RED}Back{Fore.WHITE}\n')
        else:
            pass

    def select_URL(self,bd,id):
        if bd == 'GroupsWhatsApp':
            BDGroupsW = self.db.GroupsWhatsApp.find_one({"ID":id})
            return BDGroupsW["URL"]
        elif  bd == 'GroupsTelegram':
            BDGroupsT = self.db.GroupsTelegram.find_one({"ID":id})
            return BDGroupsT["URL"]
        else:
            pass    

    def select_Admins(self,username,password):
        Admins = self.db.Admins.find()
        for a in Admins:
            if username == str(a['UserName']) and password == str(a['Password']):
                return True
            else:
                continue
        

    def Insert_Group(self,bd,name,url,DESCRIPTION):
       
        if bd == 'GroupsWhatsApp':
            num = self.db.GroupsWhatsApp.count_documents({})
            self.db.GroupsWhatsApp.insert_one({
                'ID': (int(num)+1),
                'NAME': name,
                'DESCRIPTION':DESCRIPTION,
                'URL': url,
                'STARS': 0,
                'PEOPLE_JOIN': 0
                })
        elif  bd == 'GroupsTelegram':
            num = self.db.GroupsTelegram.count_documents
            self.db.GroupsTelegram.insert_one({
                'ID': (int(num)+1),
                'NAME': name,
                'DESCRIPTION':DESCRIPTION,
                'URL': url,
                'STARS': 0,
                'PEOPLE_JOIN': 0
                })
        else:
            pass   
        

    def insert_ads(self,ad):
        self.db.Unseen.update_one({
            "ID": 1
        },{
            "$set":{"Ad":ad}   
        })

    def Add_Stars(self,bd,id):
        if bd == 'GroupsWhatsApp':
            self.db.GroupsWhatsApp.update_one({
            "ID": id
        },{
            "$inc":{"STARS": 1}   
        })
        elif  bd == 'GroupsTelegram':
            self.db.GroupsTelegram.update_one({
            "ID": 1
        },{
            "$inc":{"STARS": 1}   
        })
        else:
            pass 
   
    def Add_United(self,bd,id):
        if bd == 'GroupsWhatsApp':
            self.db.GroupsWhatsApp.update_one({
            "ID": id
        },{
            "$inc":{"PEOPLE_JOIN": 1}   
        })
        elif  bd == 'GroupsTelegram':
            self.db.GroupsTelegram.update_one({
            "ID": id
        },{
            "$inc":{"PEOPLE_JOIN": 1}   
        })
        else:
            pass 
    def select_ads(self):
        Anuncio = self.db.Unseen.find_one({"ID":1})
        return Anuncio['Ad']
    

    def select_group_All(self,bd):
        if bd == 'GroupsWhatsApp':
            database.update_database('GroupsWhatsApp')
            BDGroupsW = self.db.GroupsWhatsApp.find()
            for group in BDGroupsW:
                print(f'{Fore.BLUE}[{Fore.RED}{group["ID"]}{Fore.BLUE}] {Fore.GREEN}{group["NAME"]}\n')
        elif  bd == 'GroupsTelegram':
            database.update_database('GroupsTelegram')
            BDGroupsT = self.db.GroupsTelegram.find()
            for groupt in BDGroupsT:
                print(f'{Fore.BLUE}[{Fore.RED}{groupt["ID"]}{Fore.BLUE}] {Fore.GREEN}{groupt["NAME"]}\n')
        else:
            pass    

    def search_groups(self,search,bd):
        if bd == 'GroupsWhatsApp':
            BDGroupsW = self.db.GroupsWhatsApp.find()
            for group in BDGroupsW:
                if search.upper() in group["NAME"].upper():
                    print(f'{Fore.BLUE}[{Fore.RED}{group["ID"]}{Fore.BLUE}] {Fore.GREEN}{group["NAME"]}\n')
                else:
                    print(Fore.RED+'No results found'+Fore.RESET)
        elif  bd == 'GroupsTelegram':
            BDGroupsT = self.db.GroupsTelegram.find()
            for group in BDGroupsT:
                if search.upper() in group["NAME"].upper():
                    print(f'{Fore.BLUE}[{Fore.RED}{group["ID"]}{Fore.BLUE}] {Fore.GREEN}{group["NAME"]}\n')
                else:
                    print(Fore.RED+'No results found'+Fore.RESET)
        else:
            pass
    def SendEmail(self,name,DESCRIPTION,URL,message):
        port = 587  # For starttls
        smtp_server = "smtp-mail.outlook.com"
        sender_email = "GroupsUnseen18@outlook.es"
        receiver_email = 'termuxthorxet@gmail.com'
        password = 'unseen1845groups30050'
        message = f"""\
Subject: Solicitud de aprobacion de grupos

Name: {name}
Description: {DESCRIPTION}
URL: {URL}
Message: {message}
date: {datetime.datetime.now()}"""
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    def update_database(self,bd):
        if bd == 'GroupsWhatsApp':
            cont = 1
            GroupsW = self.db.GroupsWhatsApp.find()
            for update in GroupsW:
                self.db.GroupsWhatsApp.update_one({
                "ID": update['ID']
            },{
                "$set":{"ID": cont}   
            })
                cont += 1
        elif bd == 'GroupsTelegram':
            cont = 1
            GroupsT = self.db.GroupsTelegram.find()
            for update in GroupsT:
                self.db.GroupsTelegram.update_one({
                "ID": update['ID']
            },{
                "$set":{"ID": cont}   
            })
                cont += 1
        else:
            pass

            
        

database = DataBase()
#database.Insert_Group()

#-------------------MENU-------------------------------
                                                                                
