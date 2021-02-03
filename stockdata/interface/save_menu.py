import time
import settings
from interface import helper_functions


class Save_Menu:

    choice = None
    options = ["save", "Main Menu", "Exit"]

    def save_menu(self):
        print("\nPlease choose from the following options (enter only \nthe number):\n")
        print("1. Save report to file")
        print("2. Return to the Main Menu")
        print("3. Exit\n")

        try:
            self.choice = self.options[int(input()) - 1]
        except:
            helper_functions.validation()
        else:
            if self.choice == "save":
                print("save")
            elif self.choice == "Main Menu":
                helper_functions.restart()
            elif self.choice == "Exit":
                helper_functions.exit_app()

    def get_key(self, choice):
        settings.key = choice

    def get_value(self, choice):
        print(f"\nPlease enter the desired {choice}:\n")
        settings.value = input()

    def get_currency(self):
        print(f"\nPlease enter the three letter code for your \ndesired currency (e.g. USD, EUR):\n")
        settings.currency = input().upper()
        self.choice = "name"
