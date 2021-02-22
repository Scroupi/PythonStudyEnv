# Registration
'''
Create Login, password
Log_in, Log_out, Change_User

'''
import json
import os
class Reg:
    def __init__(self,login='check',password='check'):
        self.login = login
        self.password = password
        self.data = {'Users': []}

        # Add user to data_base
    def save_db(self):
        # Trying to handle JSONDecodeError with that funky stuff
        # I know that's dump but i couldnt find solution to 'Extra value ' problem
        # When i was opening file as 'w+' or 'r+' or 'a+'
        with open('reg_db','r') as g:
            try:
                db_data = json.load(g)
                # print('Old data -->',db_data)
            except ValueError:
                db_data = {}

        with open('reg_db', 'w') as f:
            new_data = {'login':self.login,'password':self.password}
            # print('new  data -->',new_data)
            self.data['Users'].append(new_data)
            if len(db_data) != 0:
                self.data['Users'].append(db_data['Users'][0])
            json.dump(self.data,f)
    #Read reg data_base
    def load_db(self):
        with open('reg_db', 'r') as f:
            db_data = json.load(f)
            return db_data
    # Clear data_base
    @classmethod
    def clear_db(cls):
        with open('reg_db', 'w') as n:
            pass

    def check_user(self,login:'From Log_in_window',password:'fr Log_in_window') -> bool:
        with open('reg_db', 'r') as f:
            try:
                data = json.load(f)
                res = 0
                for i in data['Users']:
                    if login == i['login'] and password == i['password']:
                        res = 1

                if res == 1:
                    return True
                else:
                    False
            except ValueError:
                print('Noone is registered yet')
                return False


# Front window
class Log_in_window(Reg):

    def __init__(self):
        super().__init__()
        self.login = ''
        self.password = ''

    # Show reg window
    def display(self):
        os.system('cls')
        print(f'Log in\nLogin: {self.login} \n\nPassword: {self.password} ')


    def get_input(self) -> bool:  # Returns Rigstr or Log in
        self.display()
        while True:
            try:
                u_inp = str(input('Are u registred? Type Y or N: '))
                break
            except ValueError as f:
                print(f'{f} error occurred, try again please')

        if u_inp.upper() == 'Y':
            return True
        else:
            return False

    def do_reg(self) -> None:
        self.display()
        while True:
            try:
                self.login = str(input('Create your login: '))
                break
            except ValueError as f:
                print(f'{f} error occurred, try again please')
        self.display()

        while True:
            try:
                self.password = str(input('Type your password: '))
                break
            except ValueError as f:
                print(f'{f} error occurred, try again please')
        self.display()
        self.save_db()

    def log_in(self) -> bool:
        self.display()
        while True:
            try:
                self.login = str(input('Type your login: '))
                break
            except ValueError as f:
                print(f'{f} error occurred, try again please')
        self.display()

        while True:
            try:
                self.password = str(input('Type your password: '))
                break
            except ValueError as f:
                print(f'{f} error occurred, try again please')
        self.display()

        if self.check_user(self.login,self.password):
            return True







