import time
import settings
from interface import main_menu, save_menu


# main_menu = main_menu.Main_Menu()


def validation():
    time.sleep(1)
    print("\nYou entered an invalid option. Try again.\n")
    time.sleep(2)
    if settings.key == None:
        menu = main_menu.Main_Menu()
        menu.main_menu()
    else:
        reset_settings()
        menu = save_menu.Save_Menu()
        menu.save_menu()


def exit_app():
    time.sleep(1)
    print("\nGoodbye.\n")
    quit()


def reset_settings():
    settings.filtered_stocks = []
    settings.stock_values = []
    settings.key = None
    settings.value = None
    settings.currency = None
