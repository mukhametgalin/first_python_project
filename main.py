import time
import os
import getpass
import random
import getch

UP = 'w'
DOWN = 's'
RIGHT = 'd'
LEFT = 'a'


def clean_console():
    os.system('clear')


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

    while result[-1] == ' ':
        result.pop()

    while result[0] == ' ':
        result.pop(0)

    return result


class Game:
    """Game"""

#   CONSTANTS

    sleep_time = 2
    money = 100
    energy = 50
    max_energy = 100
    hunger = 101
    max_hunger = 500

    def print_status(self):
        clean_console()
        print("Money: {name}".format(name=self.money))
        print("Energy: {name}/{max_en}".format(name=self.energy, max_en=self.max_energy))
        print("Hunger: {name}/{max_h}".format(name=float('{:.2f}'.format(self.hunger)), max_h=self.max_hunger))

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
        exit(0)


#   MENU_CLASS__________________________________________________________________________________________________________


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

    def get_symbol(self):
        left = time.time()
        print("\033[46mChoose your option: "
                            "{right} - go that way, {up} - go up, "
                            "{down} - go down, {left} - exit\033[0m"
                            "\nThen press ENTER\n".format(right=RIGHT, up=UP, down=DOWN, left=LEFT))
        c = getch.getch()
        print(c)
        right = time.time() - left
        self.hunger -= right
        if self.hunger < 0:
            print("\033[31mYou have lost!\n\033[0m")
            time.sleep(2)
            self.end()
        return c

    def change_energy(self, change):
        self.energy += change
        if self.energy > self.max_energy:
            self.energy = self.max_energy

    def change_hunger(self, change):
        self.hunger += change
        if self.hunger > self.max_hunger:
            self.hunger = self.max_hunger

    def game_sleep(self, sleep_time=2):
        right = sleep_time
        time.sleep(sleep_time)
        self.hunger -= right
        if self.hunger < 0:
            print("\033[31mYou have lost!\n\033[0m")
            time.sleep(2)
            self.end()


#   MINI_GAMES__________________________________________________________________________________________________________


    mini_game_hack_salary = 11
    mini_game_hack_energy_change = -20
    mini_game_dev_salary = 5
    mini_game_dev_energy_change = -10

    main_menu = Menu("Choose your activity:", "\n",
                     "->Work",
                     "->Course",
                     "->Relax",
                     "->Eat")

    work_menu = Menu("Choose your activity:", "\n",
                     "+{name}$, {name_nrg} energy points: hack code".format(
                         name=mini_game_hack_salary, name_nrg=mini_game_hack_energy_change),
                     "+{name}$ {name_nrg} energy points: develop project".format(
                         name=mini_game_dev_salary, name_nrg=mini_game_dev_energy_change))

    def mini_game_hack(self):
        clean_console()
        if self.energy + self.mini_game_hack_energy_change < 0:
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
            print("\033[34mVictory! You have received {name}$! \033[0m".format(name=self.mini_game_hack_salary))
            self.money += self.mini_game_hack_salary
        else:
            print("\033[31mYou have lost!\033[0m")
        self.change_energy(self.mini_game_hack_energy_change)
        self.game_sleep()

    def mini_game_development(self):
        clean_console()
        if self.energy + self.mini_game_dev_energy_change < 0:
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
                name=self.mini_game_dev_salary))
            self.money += self.mini_game_dev_salary
        else:
            print("\033[31mNobody needs your project!\033[0m")
        self.game_sleep()
        self.change_energy(self.mini_game_dev_energy_change)


#   COURCES_____________________________________________________________________________________________________________


    course_menu = Menu("Choose your activity:", "\n",
                       "->Development course",
                       "->Hack course")

    def do_cources(self, cource_name, cost, parameter):
        clean_console()
        print("\033[46m{cource_name} course costs"
                "\033[0m \033[32m{name}$\033[0m".format(cource_name=cource_name, name=self.development_course_cost))
        left = time.time()
        print("\033[46mDo you want to buy it \033[0m\033[43m(y/n)\033[0m\033[46m?\033[0m "
              "You will upgrade your skills.\n")
        c = getch.getch()
        right = time.time() - left
        self.hunger -= right // 1
        if self.hunger < 0:
            print("\033[31mYou have lost!\n\033[0m")
            self.game_sleep()
            self.end()
        if c == "y":
            if self.money < cost:
                clean_console()
                print("\033[31mYou can't have it\n\033[0m")
                self.game_sleep()
                return
            print("\033[34mCongratulations! Now your skill is higher\n\033[0m")
            self.game_sleep()
            self.money -= cost
            parameter += 10
            self.work_menu.menu_list[1] = "+{name}$ {name_nrg} energy points: develop project".format(
                name=self.mini_game_dev_salary, name_nrg=self.mini_game_dev_energy_change)
            return True
        else:
            return False

    development_course_cost = 100

    def development_course(self):
        fl = self.do_cources("Development", self.development_course_cost, self.mini_game_dev_salary)
        if fl:
            self.work_menu.menu_list[1] = "+{name}$ {name_nrg} energy points: develop project".format(
                name=self.mini_game_dev_salary, name_nrg=self.mini_game_dev_energy_change)

    hack_course_cost = 100

    def hack_course(self):
        fl = self.do_cources("Hacking", self.hack_course_cost, self.mini_game_hack_salary)
        if fl:
            self.work_menu.menu_list[0] = "+{name}$, {name_nrg} energy points: hack code".format(
             name=self.mini_game_hack_salary, name_nrg=self.mini_game_hack_energy_change)


#   RELAX_______________________________________________________________________________________________________________

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
            self.game_sleep(1)
        self.change_energy(self.relax_sleep_energy_change)
        finish = self.energy
        print("\033[34m{name} energy points restored!\033[0m".format(name=finish - start))
        self.game_sleep()

    club_cost = 30

    def relax_restoring(self, activity, cost, change, full_relax=False):
        clean_console()
        start = self.energy
        print("\033[46mYou want to {activity}, it costs\033[0m "
              "\033[32m{name}$\033[0m".format(activity=activity, name=cost))
        left = time.time()
        print("\033[46mDo you want to {activity} \033[0m\033[43m(y/n)\033[0m\033[46m?\033[0m"
                            " You will restore your energy\n".format(activity=activity))
        c = getch.getch()
        right = time.time() - left
        self.hunger -= right // 1
        if self.hunger < 0:
            print("\033[31mYou have lost!\n\033[0m")
            self.game_sleep()
            self.end()
        if c == "y":
            if self.money < cost:
                clean_console()
                print("\033[31mYou can't {activity}\n\033[0m".format(activity=activity))
                self.game_sleep()
            else:
                if full_relax:
                    print("\033[34mCongratulations! Now your energy is 100%\n\033[0m")
                    self.game_sleep()
                    self.money -= cost
                    self.energy = self.max_energy
                else:
                    self.change_energy(change)
                    finish = self.energy
                    print("\033[34m{name} energy points restored!\033[0m".format(name=finish - start))
                    self.game_sleep()

    def relax_go_to_the_club(self):
        self.relax_restoring("go to the club", self.club_cost, 0, True)


#   EAT_________________________________________________________________________________________________________________

    eat_menu = Menu("Choose your activity:", "\n",
                      "->Eat doshirak",
                      "->Go to the cafe",
                      "->Go to the restaurant")

    doshirak_cost = 2
    doshirak_change = 50

    def hunger_restoring(self, activity, cost, change):
        clean_console()
        start = self.hunger
        print("\033[46mYou want to {some}, it costs"
              "\033[0m \033[32m{name}$\033[0m".format(some=activity, name=cost))
        left = time.time()
        print("\033[46mDo you want to {activity} \033[0m\033[43m(y/n)\033[0m\033[46m?\033[0m"
                            " You will restore {name} points of hunger\n".format(activity=activity, name=change))
        c = getch.getch()
        right = time.time() - left
        self.hunger -= right // 1
        if self.hunger < 0:
            print("\033[31mYou have lost!\n\033[0m")
            self.game_sleep()
            self.end()
        if c == "y":
            if self.money < cost:
                clean_console()
                print("\033[31mYou can't {activity}\n\033[0m".format(activity=activity))
                self.game_sleep()
            else:
                self.money -= cost
                self.change_hunger(change)
                finish = self.hunger
                print("\033[34m{name} hunger points restored!"
                      "\033[0m".format(name=float('{:.3f}'.format(finish - start))))
                self.game_sleep()

    def eat_doshirak(self):
        self.hunger_restoring("eat doshirak", self.doshirak_cost, self.doshirak_change)

    cafe_cost = 10
    cafe_change = 200

    def cafe(self):
        self.hunger_restoring("go to the cafe", self.cafe_cost, self.cafe_change)

    restaurant_cost = 30
    restaurant_change = 1000

    def restaurant(self):
        self.hunger_restoring("go to the restaurant", self.restaurant_cost, self.restaurant_change)


#   RUN_________________________________________________________________________________________________________________

    def run_some_option(self, cur_menu, *args):
        clean_console()
        cur_menu.print_menu()
        c = self.get_symbol()
        if c == DOWN:
            cur_menu.down_mark()
        elif c == UP:
            cur_menu.up_mark()
        elif c == RIGHT:
            pointer = 0
            for i in args:
                if cur_menu.marker == pointer:
                    i()
                    break
                pointer += 1

        elif c == LEFT:
            return False
        return True

    def run(self):
        self.introduce()
        while True: #event loop
            self.print_status()
            self.main_menu.print_menu()
            c = self.get_symbol()
            if c == DOWN:
                self.main_menu.down_mark()
            elif c == UP:
                self.main_menu.up_mark()
            elif c == RIGHT:
                if self.main_menu.marker == 0:
                    while True:
                        fl = self.run_some_option(self.work_menu, self.mini_game_hack, self.mini_game_development)
                        if not fl:
                            break
                elif self.main_menu.marker == 1:
                    while True:
                        fl = self.run_some_option(self.course_menu, self.development_course, self.hack_course)
                        if not fl:
                            break
                elif self.main_menu.marker == 2:
                    while True:
                        fl = self.run_some_option(self.relax_menu, self.relax_sleep, self.relax_go_to_the_club)
                        if not fl:
                            break
                elif self.main_menu.marker == 3:
                    while True:
                        fl = self.run_some_option(self.eat_menu, self.eat_doshirak, self.cafe, self.restaurant)
                        if not fl:
                            break
            elif c == LEFT:
                break
        self.end()


a = Game()
a.run()
