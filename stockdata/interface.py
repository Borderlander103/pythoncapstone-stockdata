import time


class Interface:

    options = ["name", "industry", "market"]

    def welcome(self):
        print("\n\n\n\n\n\n\n    --- Stock Data Reports --- \n")
        print("This small utility will provide basic reports based on ")
        print("imported stock data.\n")

    def main_menu(self):
        # options = ["name", "industry", "market"]
        print("Please choose from the following options (enter only \nthe number):\n")
        print("1. Lookup by name")
        print("2. Lookup by industry")
        print("3. Lookup by market\n")
        choice = self.options[int(input()) - 1]
        print(f"\nOkay, looking up by {choice}.")
        time.sleep(3)
        print("Give me a second...")
        time.sleep(3)

    def main_validation(self):
        pass
