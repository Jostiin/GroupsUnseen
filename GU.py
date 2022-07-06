import pymysql
from colorama import init, Fore, Back, Style
from pyfiglet import Figlet

init(convert=True)
#----------------------------MYSQL-----------------------------------
class DataBase:

    def __init__(self):
        self.connection = pymysql.connect(
        host="83lfaety6ex9.us-east-4.psdb.cloud",#------
        user="x8qt7ftgcp5y",#--
        password="pscale_pw_GI123oAl3_0sqahW_KhjdgsVLDdPQcwAx24b029mP8w",#----
        database="kaliproject",#--
        port=3306)
        self.cursor = self.connection.cursor()
        

    def select_group_One(self,bd,id):
        sql = f'SELECT Name, URL,stars,review,United FROM {bd} WHERE {id}'
        try:
            self.cursor.execute(sql)
            group = self.cursor.fetchone()
            custom_fig = Figlet(font=str('standard'))
            print(custom_fig.renderText(f'{group[0]}'))
            print(f'{Fore.BLUE}{group[3]}\n\nURL{Fore.WHITE}:{Fore.GREEN} {group[1]}\n')
            print(f'{Fore.YELLOW}({group[2]})Stars\n')
            print(f'{Fore.WHITE}{group[4]} people have joined\n')
            print(f'{Fore.BLUE}[{Fore.RED}100{Fore.BLUE}] {Fore.GREEN}Join Group')
            print(f'{Fore.BLUE}[{Fore.RED}300{Fore.BLUE}] {Fore.YELLOW}Qualify')
            print(f'{Fore.BLUE}[{Fore.RED}200{Fore.BLUE}] {Fore.RED}Back{Fore.WHITE}\n')
        except Exception as es:
            raise

    def select_URL(self,bd,id):
        sql = f'SELECT URL FROM {bd} WHERE {id}'
        try:
            self.cursor.execute(sql)
            group = self.cursor.fetchone()
            return group[0]
        except Exception as es:
            raise

    def select_Admins(self,bd,username,password):
        sql = f'SELECT username,password FROM {bd}'
        try:
            self.cursor.execute(sql)
            admin = self.cursor.fetchone()
            if username == admin[0] and password == admin[1]:
                return True
        except Exception as es:
            raise

    def Insert_Group(self,bd,name,url,review,stars):

        sql = f"INSERT INTO {bd}(Name,URL,review,stars) VALUES ('{name}','{url}','{review}','{stars}')"
        try:
            self.cursor.execute(sql)
            self.cursor.connection.commit()
            print('\nGrupo Insertado Correctamente')
        except Exception as es:
            raise
    def insert_ads(self,ad):
        sql = f"UPDATE groupsunseen SET Ads='{ad}' WHERE id_sql = 1"
        try:
            self.cursor.execute(sql)
            self.cursor.connection.commit()
            print('\nAnuncio Actualizado correctamente')
        except Exception as es:
            raise
    def Add_Stars(self,bd,id):
        sql = f"SELECT stars FROM {bd} WHERE id_sql = {id}"
        try:
            self.cursor.execute(sql)
            stars = self.cursor.fetchone()

        except Exception as es:
            raise
        
        sql = f"UPDATE {bd} SET stars={(int(stars[0])+1)} WHERE id_sql = '{id}'"
        try:
            self.cursor.execute(sql)
            self.cursor.connection.commit()
            
        except Exception as es:
            raise
    def Add_United(self,bd,id):
        sql = f"SELECT United FROM {bd} WHERE id_sql = {id}"
        try:
            self.cursor.execute(sql)
            united = self.cursor.fetchone()

        except Exception as es:
            raise

        sql = f"UPDATE {bd} SET United={(int(united[0])+1)} WHERE id_sql = '{id}'"
        try:
            self.cursor.execute(sql)
            self.cursor.connection.commit()
            
        except Exception as es:
            raise
    def select_ads(self):
        sql = f'SELECT Ads FROM groupsunseen'
        try:
            self.cursor.execute(sql)
            ads = self.cursor.fetchone()
            return ads
        except Exception as es:
            raise
    def select_group_All(self,bd):
        sql = f'SELECT id_sql, Name, URL FROM {bd}'
        try:
            self.cursor.execute(sql)
            groups = self.cursor.fetchall()
            for group in groups:
                print(f'{Fore.BLUE}[{Fore.RED}{group[0]}{Fore.BLUE}] {Fore.GREEN}{group[1]}\n')
        except Exception as es:
            raise
    def search_groups(self,search,bd):
        sql = f'SELECT id_sql, Name FROM {bd}'
        try:
            self.cursor.execute(sql)
            groups = self.cursor.fetchall()
            for group in groups:   
                if search.upper() in group[1].upper():
                    print(f'{Fore.BLUE}[{Fore.RED}{group[0]}{Fore.BLUE}] {Fore.GREEN}{group[1]}\n')
                else:
                    print(Fore.RED+'No results found'+Fore.RESET)
            
        except Exception as es:
            raise


database = DataBase()

#-------------------MENU-------------------------------
                                                                                
