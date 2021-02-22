# Registration
'''
Create Login, password
Log_in, Log_out, Change_User

'''
import json
import os
class Reg:
    def __init__(self,login,password):
        self.login = login
        self.password = password
        self.data = {'Users': []}

    def save_db(self):
        # Trying to handle JSONDecodeError with that funky stuff
        # I know that's dump but i couldnt find solution to 'Extra value ' problem
        # When i was opening file as 'w+' or 'r+' or 'a+'
        with open('reg_db','r') as g:
            try:
                db_data = json.load(g)
                print('Old data -->',db_data)
            except ValueError:
                db_data = {}

        with open('reg_db', 'w') as f:
            new_data = {'login':self.login,'password':self.password}
            print('new  data -->',new_data)
            self.data['Users'].append(new_data)
            if len(db_data) != 0:
                self.data['Users'].append(db_data['Users'])
            json.dump(self.data,f)

    def load_db(self):
        with open('reg_db', 'r') as f:
            db_data = json.load(f)
            print(db_data)
    @classmethod
    def clear_db(cls):
        with open('reg_db', 'w') as n:
            pass


# user_1 = Reg('Iliy', 1111)
# user_1.save_db()
# # user_1.load_db()
# user_2 = Reg('Foo',2333)
# user_2.save_db()
# # user_2.load_db()
Reg.clear_db()
# user_5 = Reg('Shrek', 228)
# user_5.save_db()
# user_5.load_db()
