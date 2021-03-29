import time
import os
import getpass
import random
UP = '\x1b[A'
DOWN = '\x1b[B'
RIGHT = '\x1b[C'
LEFT = '\x1b[D'


def clean_console():
    os.system('clear')


def game_sleep(self):
    time.sleep(self.sleep_time)


def generate_text():
    chars = []
    for i in range(ord('a'), ord('z') + 1):
        chars.append(chr(i))
    for i in range(ord('A'), ord('A') + 1):
        chars.append(chr(i))
    for i in range(ord('0'), ord('9') + 1):
        chars.append(chr(i))
    chars.append(' ')

    default_size = 20

    result = ""

    for i in range(default_size):
        result = result + chars[random.randrange(0, len(chars))]

    return result


class Game:
    """Game"""

    sleep_time = 2
    money = 100
    energy = 50
    max_energy = 100
   # exp = 10

    def print_status(self):
        clean_console()
        print("Money: {name}".format(name=self.money))
        print("Energy: {name}/{max_en}".format(name=self.energy, max_en=self.max_energy))
       # print("Exp: {name}".format(name=self.exp))

    def introduce(self):
        clean_console()
        print("""
\033[1;36mHey! 
This is my game - programmer simulator. 
Here you will not learn anything, but you will have a good rest. Hope you enjoy it!\033[0m
        """)
        time.sleep(6)
        clean_console()

    def end(self):
        clean_console()
        print("\033[1;36mBye bye\033[0m")
        time.sleep(self.sleep_time)

    class Menu:
        """Menu"""
        header = ""
        final_message = ""
        menu_list = []
        marker = 0

        def __init__(self, header, final_message, *menu_list):
            self.header = header
            self.final_message = final_message
            self.menu_list = list(menu_list)

        def down_mark(self):
            if self.marker != len(self.menu_list) - 1:
                self.marker += 1

        def up_mark(self):
            if self.marker != 0:
                self.marker -= 1

        def print_menu(self):
            print(self.header)
            for i in range(len(self.menu_list)):
                if i == self.marker:
                    print('\x1b[30;42m' + self.menu_list[i] + '\x1b[0m')
                else:
                    print(self.menu_list[i])
            print(self.final_message)

    def change_energy(self, change):
        self.energy += change
        if self.energy > self.max_energy:
            self.energy = self.max_energy

    mini_game_hack_salary = 11
    mini_game_hack_energy_change = -20
    mini_game_dev_salary = 5
    mini_game_dev_energy_change = -10

    main_menu = Menu("Choose your activity:", "\n",
                     "->Work",
                     "->Course",
                     "->Relax")

    work_menu = Menu("Choose your activity:", "\n",
                     "+{name}$, {name_nrg} energy points: hack code".format(
                         name=mini_game_hack_salary, name_nrg=mini_game_hack_energy_change),
                     "+{name}$ {name_nrg} energy points: develop project".format(
                         name=mini_game_dev_salary, name_nrg=mini_game_dev_energy_change))

    def mini_game_hack(self):
        clean_console()
        if self.energy + self.mini_game_hack_energy_change < 0:
            print('\x1b[31m' + "You can't do it." + '\x1b[0m')
            time.sleep(self.sleep_time)
            return
        text = generate_text()
        print(text)
        print("\033[46mHere is a sequence of characters that will help you hack someone else's system.\033[0m")
        x = getpass.getpass("\033[46mTo hack the system, repeat the sequence:\033[0m ")
        if x == text:
            print("\033[34mVictory! You have received {name}$! \033[0m".format(name=self.mini_game_hack_salary))
            self.money += self.mini_game_hack_salary
        else:
            print("\033[31mYou have lost!\033[0m")
        self.change_energy(self.mini_game_hack_energy_change)
        time.sleep(self.sleep_time)

    def mini_game_development(self):
        clean_console()
        if self.energy + self.mini_game_dev_energy_change < 0:
            print('\x1b[36m' + "You can't do it" + '\x1b[0m')
            time.sleep(self.sleep_time)
            return
        print("\033[46mDevelop a project and try to sell it:\033[0m")
        prj = getpass.getpass("\033[46mEnter a sequence of characters: "
                              "the longer it is, the more chances you have to sell the project.\n\033[0m")

        clean_console()
        len_prj = min(len(prj), 100)
        x = random.randrange(1, 101, 1)
        if (x <= len_prj):
            print("\x1b[34mCongratulations! you sold the project! Your earnings: +{name}$ \x1b[0m".format(
                name=self.mini_game_dev_salary))
            self.money += self.mini_game_dev_salary
        else:
            print("\033[31mNobody needs your project!\033[0m")
        time.sleep(self.sleep_time)
        self.change_energy(self.mini_game_dev_energy_change)

    course_menu = Menu("Choose your activity:", "\n",
                       "->Development course",
                       "->Hack course")

    development_course_cost = 100
    
    def development_course(self):
        clean_console()
        print("\033[46mDevelopment course costs\033[0m \033[32m{name}$\033[0m".format(name=self.development_course_cost))
        c = getpass.getpass("\033[46mDo you want to buy it \033[0m\033[43m(y/n)\033[0m\033[46m?\033[0m "
                            "You will upgrade your skills.\n")
        if c == "y":
            if self.money < self.development_course_cost:
                clean_console()
                print("\033[31mYou can't have it\n\033[0m")
                time.sleep(self.sleep_time)
                return
            print("\033[34mCongratulations! Now your skill is higher\n\033[0m")
            time.sleep(self.sleep_time)
            self.money -= self.development_course_cost
            self.mini_game_dev_salary += 10
            self.work_menu.menu_list[1] = "+{name}$ {name_nrg} energy points: develop project".format(
                         name=self.mini_game_dev_salary, name_nrg=self.mini_game_dev_energy_change)
        else:
            return
        
    hack_course_cost = 100

    def hack_course(self):
        clean_console()
        print("\033[46mHack course costs\033[0m \033[32m{name}$\033[0m".format(name=self.hack_course_cost))
        c = getpass.getpass("\033[46mDo you want to buy it \033[0m\033[43m(y/n)\033[0m\033[46m?\033[0m"
                            " You will upgrade your skills.\n")
        if c == "y":
            if self.money < self.hack_course_cost:
                clean_console()
                print("\033[31mYou can't have it\n\033[0m")
                time.sleep(self.sleep_time)
                return
            print("\033[34mCongratulations! Now your skill is higher\n\033[0m")
            time.sleep(self.sleep_time)
            self.money -= self.hack_course_cost
            self.mini_game_hack_salary += 10
            self.work_menu.menu_list[0] = "+{name}$, {name_nrg} energy points: взломать код".format(
                         name=self.mini_game_hack_salary, name_nrg=self.mini_game_hack_energy_change)
        else:
            return

    relax_menu = Menu("Choose your activity:", "\n",
                      "->Sleep",
                      "->Go to the club")

    time_of_relax_sleep = 8
    relax_sleep_energy_change = 2

    def relax_sleep(self):
        start = self.energy
        for i in range(self.time_of_relax_sleep, 0, -1):
            clean_console()
            print("\033[46mYou are sleeping now, wait for {name} seconds\033[0m".format(name=i))
            time.sleep(1)
        self.change_energy(self.relax_sleep_energy_change)
        finish = self.energy
        print("\033[34m{name} energy points restored!\033[0m".format(name=finish - start))
        time.sleep(self.sleep_time)


    club_cost = 30

    def relax_go_to_the_club(self):
        clean_console()
        print("\033[46mYou want to go to the club, it costs\033[0m \033[32m{name}$\033[0m".format(name=self.club_cost))
        c = getpass.getpass("\033[46mDo you want to go to the club \033[0m\033[43m(y/n)\033[0m\033[46m?\033[0m"
                            " You will restore your energy\n")
        if c == "y":
            if self.money < self.club_cost:
                clean_console()
                print("\033[31mYou can't go to the club\n\033[0m")
                time.sleep(self.sleep_time)
            else:
                print("\033[34mCongratulations! Now your energy is 100%\n\033[0m")
                time.sleep(self.sleep_time)
                self.money -= self.club_cost
                self.energy = self.max_energy

    def run(self):
        self.introduce()
        while True:
            self.print_status()
            self.main_menu.print_menu()
            c = getpass.getpass("\033[46mChoose your option: "
                                "right arrow - go that way, up arrow - go up, "
                                "down arrow - go down, left arrow - exit\033[0m"
                                "\nThen press ENTER\n")
            if c == DOWN:
                self.main_menu.down_mark()
            elif c == UP:
                self.main_menu.up_mark()
            elif c == RIGHT:
                if self.main_menu.marker == 0:
                    while True:
                        clean_console()
                        self.work_menu.print_menu()
                        c = getpass.getpass("\033[46mChoose your option: "
                                            "right arrow - go that way, up arrow - go up, "
                                            "down arrow - go down, left arrow - exit\033[0m"
                                            "\nThen press ENTER\n")
                        if c == DOWN:
                            self.work_menu.down_mark()
                        elif c == UP:
                            self.work_menu.up_mark()
                        elif c == RIGHT:
                            if self.work_menu.marker == 0:
                                self.mini_game_hack()
                            else:
                                self.mini_game_development()
                        elif c == LEFT:
                            break
                elif self.main_menu.marker == 1:
                    while True:
                        clean_console()
                        self.course_menu.print_menu()
                        c = getpass.getpass("\033[46mChoose your option: "
                                            "right arrow - go that way, up arrow - go up, "
                                            "down arrow - go down, left arrow - exit\033[0m"
                                            "\nThen press ENTER\n")
                        if c == DOWN:
                            self.course_menu.down_mark()
                        elif c == UP:
                            self.course_menu.up_mark()
                        elif c == RIGHT:
                            if self.course_menu.marker == 0:
                                self.development_course()
                            if self.course_menu.marker == 1:
                                self.hack_course()
                            else:
                                pass
                        elif c == LEFT:
                            break
                elif self.main_menu.marker == 2:
                    while True:
                        clean_console()
                        self.relax_menu.print_menu()
                        c = getpass.getpass("\033[46mChoose your option: "
                                            "right arrow - go that way, up arrow - go up, "
                                            "down arrow - go down, left arrow - exit\033[0m"
                                            "\nThen press ENTER\n")
                        if c == DOWN:
                            self.relax_menu.down_mark()
                        elif c == UP:
                            self.relax_menu.up_mark()
                        elif c == RIGHT:
                            if self.relax_menu.marker == 0:
                                self.relax_sleep()
                            if self.relax_menu.marker == 1:
                                self.relax_go_to_the_club()
                                pass
                        elif c == LEFT:
                            break
            elif c == LEFT:
                break
        self.end()


a = Game()
a.run()
