import time
from interface import main_menu


# main_menu = main_menu.Main_Menu()


def main_validation():
    time.sleep(1)
    print("\nYou entered an invalid option. Try again.\n")
    time.sleep(2)
    menu = main_menu.Main_Menu()
    menu.main_menu()


def exit_app():
    time.sleep(1)
    print("\nGoodbye.\n")
    quit()
