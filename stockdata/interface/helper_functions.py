import time
from interface import main_menu


def main_validation(self):
    time.sleep(1)
    print("\nYou entered an invalid option. Try again.\n")
    time.sleep(2)
    main_menu.main_menu()


def exit_app():
    time.sleep(1)
    print("\nGoodbye.\n")
    quit()
