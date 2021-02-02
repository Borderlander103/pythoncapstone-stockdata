import settings
import time


class Main_Menu:

    choice = None
    options = ["name", "industry",
               "market", "currency", "Exit"]

    def main_menu(self):
        print("Please choose from the following options (enter only \nthe number):\n")
        print("1. Lookup report by name")
        print("2. Lookup report by industry")
        print("3. Lookup report by market")
        print("4. Convert currency of given stock")
        print("5. Exit\n")
        try:
            self.choice = self.options[int(input()) - 1]
        except:
            self.main_validation()
        else:
            if self.choice == "Exit":
                print("\nGoodbye.\n")
                quit()
            if self.choice == "currency":
                self.get_currency()
            self.get_key(self.choice)
            self.get_value(self.choice)
            # return (self.key, self.value, self.currency)
            # print(settings.key, settings.value, settings.currency)

    def get_key(self, choice):
        settings.key = choice

    def get_value(self, choice):
        print(f"\nPlease enter the desired {choice}:\n")
        settings.value = input()

    def get_currency(self):
        print(f"\nPlease enter the three letter code for your \ndesired currency (e.g. USD, EUR):\n")
        settings.currency = input().upper()
        self.choice = "name"

    def main_validation(self):
        time.sleep(1)
        print("\nYou entered an invalid option. Try again.\n")
        time.sleep(2)
        self.main_menu()
