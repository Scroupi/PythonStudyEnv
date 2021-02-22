# Math_Game

''' Structure:
    Reg_window
    {Log_in
    or  Registration}
    Score_Board
    Difficulty
    Main_Game

    User path:
    Log_in_window --> Reg or log_in --> Game(User) --> ***
    Change difficulty(defines in Game) --> Exit
'''
from Account_utilities import User
import random, os, time
class Game_engine:
    def __init__(self,difficulty):
        ' 1: Ease, 2: normal, 3:hard'
        self.difficulty = difficulty

    def get_equation(self):
        data = []
        for i in range(self.difficulty + 1):
            data.append(random.randrange(10))
        self.equation = [''.join(str(i)) if i != 0 else ''.join(str(i+1)) for i in data]
        self.equation = ''.join(self.equation)

        return int(self.equation)

    def change_difficulty(self):
        self.difficulty = int(input('Choose difficulty between 1 to 3: '))

    def mod_changer(self):
        self.mode = random.randint(0,2)
        if self.mode == 0:
            return '+'
        elif self.mode == 1:
            return '-'
        elif self.mode == 2:
            return '*'

    def display_task(self):
        # os.system('cls')
        self.current_mod = self.mod_changer()
        self.current_eq1 = self.get_equation()
        self.current_eq2 = self.get_equation()
        print('*********\n',self.current_eq1,'\n',self.current_mod,'\n',self.current_eq2,'\n*********')

    def get_input(self):
        while True:
            try:
                self.answer = (input('Your answer:   '))
                if self.answer == 'reset':
                    self.change_difficulty()
                    self.answer = int((input('Your answer:  ')))
                self.answer = int(self.answer)
                break
            except Exception as f:
                print(f'{f} error occurred, try again please')

    def check_answer(self):
        if self.current_mod == '+':
            answer = self.current_eq1 + self.current_eq2
        elif self.current_mod == '-':
            answer = self.current_eq1 - self.current_eq2
        elif self.current_mod == '*':
            answer = self.current_eq1 * self.current_eq2


        if answer == int(self.answer):
            print('Correct')
            time.sleep(0.5)
            return True
        else:
            print('Wrong')
            time.sleep(0.5)
            return False



class Game:

    def __init__(self):
        self.u_obj = User()
        self.game_engine = Game_engine(1)

    def display(self):
        os.system('cls')
        print(f'Current user:  {self.u_obj.name}                   Press "CTRL+C" to end the game\n                                     Type "reset" to change difficulty')
        self.game_engine.display_task()
        print(f'Score: {self.u_obj.score} ')
    def run_game(self):
        self.u_obj.define_user()
        while True:
            self.display()
            self.game_engine.get_input()
            if self.game_engine.check_answer():
                self.u_obj.score += 1
            else:
                self.u_obj.score -= 1



if __name__ == '__main__':
    game = Game()
    game.run_game()
