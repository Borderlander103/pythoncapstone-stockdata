import report_creator
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
            report = report_creator.Report_Creator()
            if self.choice == "save":
                report.save_report()
                report.clear_report()
                helper_functions.restart()
            elif self.choice == "Main Menu":
                report.clear_report()
                helper_functions.restart()
            elif self.choice == "Exit":
                helper_functions.exit_app()
