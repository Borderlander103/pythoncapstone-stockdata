import time


class Interface:

    options = ["name", "industry", "market", "Quit"]

    def welcome(self):
        print("\n\n\n\n\n\n\n    --- Stock Data Reports --- \n")
        print("This small utility will provide basic reports based on ")
        print("imported stock data.\n")

    def main_menu(self):
        print("Please choose from the following options (enter only \nthe number):\n")
        print("1. Lookup by name")
        print("2. Lookup by industry")
        print("3. Lookup by market")
        print("4. Quit\n")
        try:
            choice = self.options[int(input()) - 1]
        except:
            self.main_validation()
        else:
            if choice == "Quit":
                print("\nGoodbye.\n")
                quit()
            print(f"\nOkay, looking up by {choice}.")
            time.sleep(2)
            print("Give me a second...")
            time.sleep(2)

    def main_validation(self):
        time.sleep(1)
        print("\nYou entered an invalid option. Try again.\n")
        time.sleep(2)
        self.main_menu()
