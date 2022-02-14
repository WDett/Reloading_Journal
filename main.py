from colorama import init
import os
import menus.menu_main as menu_main
import sql_handler.sql_handler as sql_handler


version = 'v0.1'


if __name__ == '__main__':
    os.system('mode con: cols=120 lines=33')
    init(convert=True)
    sql_handler.initialize_sqlite()
    menu_main.display()

