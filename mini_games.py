import time
import getpass
from helping_module import clean_console
from helping_module import generate_text
import random

mini_game_hack_salary = 11
mini_game_hack_energy_change = -20
mini_game_dev_salary = 5
mini_game_dev_energy_change = -10


def mini_game_hack(self):
    clean_console()
    if self.energy + mini_game_hack_energy_change < 0:
        print('\x1b[31m' + "You can't do it." + '\x1b[0m')
        self.game_sleep()
        return
    text = generate_text()
    print(text)
    print("\033[46mHere is a sequence of characters that will help you hack someone else's system.\033[0m")
    left = time.time()
    x = getpass.getpass("\033[46mTo hack the system, repeat the sequence:\033[0m ")
    right = time.time() - left
    self.hunger -= right // 1
    if self.hunger < 0:
        print("\033[31mYou have lost!\n\033[0m")
        self.game_sleep()
        self.end()
    if x == text:
        print("\033[34mVictory! You have received {name}$! \033[0m".format(name= mini_game_hack_salary))
        self.money += mini_game_hack_salary
    else:
        print("\033[31mYou have lost!\033[0m")
    self.change_energy(mini_game_hack_energy_change)
    self.game_sleep()


def mini_game_development(self):
    clean_console()
    if self.energy + mini_game_dev_energy_change < 0:
        print('\x1b[36m' + "You can't do it" + '\x1b[0m')
        self.game_sleep()
        return
    print("\033[46mDevelop a project and try to sell it:\033[0m")
    left = time.time()
    prj = input("\033[46mEnter a sequence of characters: "
                "the longer it is, the more chances you have to sell the project.\n\033[0m")
    right = time.time() - left
    self.hunger -= right // 1
    if self.hunger < 0:
        print("\033[31mYou have lost!\n\033[0m")
        self.game_sleep()
        self.end()

    clean_console()
    len_prj = min(len(prj), 100)
    x = random.randrange(1, 101, 1)
    if x <= len_prj:
        print("\x1b[34mCongratulations! you sold the project! Your earnings: +{name}$ \x1b[0m".format(
            name=mini_game_dev_salary))
        self.money += mini_game_dev_salary
    else:
        print("\033[31mNobody needs your project!\033[0m")
    self.game_sleep()
    self.change_energy(mini_game_dev_energy_change)