import time
import settings
from interface import save_menu


def validation():
    time.sleep(1)
    print("\nYou entered an invalid option. Try again.\n")
    time.sleep(2)
    if settings.key == None:
        restart()
    else:
        menu = save_menu.Save_Menu()
        menu.save_menu()


def exit_app():
    time.sleep(1)
    print("\nGoodbye.\n")
    quit()


def restart():
    import app
    reset_settings()
    menu = app.App()
    menu.app()


def reset_settings():
    settings.filtered_stocks = []
    settings.stock_values = []
    settings.key = None
    settings.value = None
    settings.currency = None
