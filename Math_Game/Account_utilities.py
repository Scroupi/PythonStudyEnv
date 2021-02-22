# Account utilities

# Classes : User, scoreboard
from Utility import Log_in_window, Reg
import json, time
class User:
    def __init__(self):
        self.f = Log_in_window() # My first usage of composition dunno if its valid here
        self.score = 0
    def define_user(self):
        while True:
            if self.f.get_input():
                if self.f.log_in():
                    print('You logged in')
                    time.sleep(0.5)
                    break
                else:
                    print('Wrong login or password, try again')
                    time.sleep(1)
            else:
                self.f.do_reg()
        self.name = self.f.login


    def score_to_db(self):
        with open('score_db', 'r') as f:
            if len(f) != 0:
                data = json.load(f)
            else: pass

        with open('score_db', 'w') as g:
            data = {self.name:self.score}

            json.dump(data, f)




