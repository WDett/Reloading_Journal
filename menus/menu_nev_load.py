import menus.menu_global_commands as menu_global_commands
import sql_handler.sql_handler as sql_handler
import menus.menu_main as menu_main
import menus.menu_select_load as menu_select_load
import pdf_handler.pdf_handler_load_data as pdf_handler_load_data
import textwrap
from datetime import datetime
from colorama import Fore, Style

now = datetime.now()
global data_entered


def display_refresh(current_input_location, view_function):
    command_list = ''
    if view_function == 'new':
        command_list = ['q', 'c', 's']
    if view_function == 'edit':
        command_list = ['q', 'c', 's', 'd']
    if view_function == 'view':
        command_list = ['q', 'b', 'e', 'p', 'l']

    options_and_commands_list = command_list
    user_input_command = ""
    menu_global_commands.clear_console()
    menu_global_commands.display_title("LOAD DATA")
    print("\n   " + Fore.CYAN + "LOAD " + Style.RESET_ALL)
    print("{: <5} {: >15} {: <45} {: >10} {: <20}".format('', Fore.GREEN + "NAME:", Fore.WHITE + data_entered[1],
                                                          Fore.GREEN + "ID #:", Fore.WHITE + data_entered[0] +
                                                          Style.RESET_ALL))
    print("{: <5} {: >15} {: <20} {: >14} {: <15} {: >14} {: <15}".format('', Fore.GREEN + "CARTRIDGE:", Fore.WHITE +
                                                                          data_entered[2], Fore.GREEN + "COAL:",
                                                                          Fore.WHITE + data_entered[3], Fore.GREEN +
                                                                          "VELOCITY:", Fore.WHITE + data_entered[4] +
                                                                          Style.RESET_ALL))

    print("\n   " + Fore.CYAN + "BRASS " + Style.RESET_ALL)
    print("{: <5} {: >15} {: <20} {: >14} {: <15} {: >14} {: <15}".format('', Fore.GREEN + "BRAND:", Fore.WHITE +
                                                                          data_entered[5], Fore.GREEN + "FIRINGS:",
                                                                          Fore.WHITE + data_entered[6], Fore.GREEN +
                                                                          "LENGTH:", Fore.WHITE + data_entered[7] +
                                                                          Style.RESET_ALL))
    print("{: <5} {: >15} {: <20} {: >14} {: <15} {: >14} {: <15}".format('', Fore.GREEN + "TUMBLED:", Fore.WHITE +
                                                                          data_entered[8], Fore.GREEN + "ANNEALED:",
                                                                          Fore.WHITE + data_entered[9], Fore.GREEN +
                                                                          "TRIMMED:", Fore.WHITE + data_entered[10] +
                                                                          Style.RESET_ALL))
    print("{: <5} {: >15} {: <20} {: >14} {: <15} {: >14} {: <15}".format('', Fore.GREEN + "CHAMFER:", Fore.WHITE +
                                                                          data_entered[11], Fore.GREEN + "DEBURRED:",
                                                                          Fore.WHITE + data_entered[12], Fore.GREEN +
                                                                          "CRIMP:", Fore.WHITE + data_entered[13] +
                                                                          ' @ ' + data_entered[14] + Style.RESET_ALL))

    print("\n   " + Fore.CYAN + "PRIMER " + Style.RESET_ALL)
    print("{: <5} {: >15} {: <20} {: >14} {: <15} ".format('', Fore.GREEN + "BRAND:", Fore.WHITE + data_entered[15],
                                                           Fore.GREEN + "MODEL:", Fore.WHITE + data_entered[16] +
                                                           Style.RESET_ALL))

    print("\n   " + Fore.CYAN + "POWDER " + Style.RESET_ALL)
    print("{: <5} {: >15} {: <20} {: >14} {: <15} {: >14} {: <15}".format('', Fore.GREEN + "BRAND:", Fore.WHITE +
                                                                          data_entered[17], Fore.GREEN + "MODEL:",
                                                                          Fore.WHITE + data_entered[18], Fore.GREEN +
                                                                          "GRAINS:", Fore.WHITE + data_entered[19] +
                                                                          Style.RESET_ALL))

    print("\n   " + Fore.CYAN + "PROJECTILE " + Style.RESET_ALL)
    print("{: <5} {: >15} {: <20} {: >14} {: <15} {: >14} {: <15}".format('', Fore.GREEN + "BRAND:", Fore.WHITE +
                                                                          data_entered[20], Fore.GREEN + "MODEL:",
                                                                          Fore.WHITE + data_entered[21], Fore.GREEN +
                                                                          "GRAINS:", Fore.WHITE + data_entered[22] +
                                                                          Style.RESET_ALL))

    print("\n   " + Fore.CYAN + "NOTES " + Style.RESET_ALL)
    print(Fore.WHITE + textwrap.fill(data_entered[23], 110, initial_indent='      ', subsequent_indent='      ') +
          Style.RESET_ALL)
    if len(data_entered[23]) <= 110:
        print('\n\n')
    elif len(data_entered[23]) <= 220:
        print('\n')
    elif len(data_entered[23]) <= 330:
        print('')
    process_input(options_and_commands_list, current_input_location, view_function)


def display(view_function, load_id):
    global data_entered
    data_entered = [''] * 24
    if load_id != '0':
        data_entered[0] = load_id

    if view_function == 'edit':
        data_entered = sql_handler.get_load_by_id(load_id)
        current_input_location = 1
        while current_input_location < 24:
            display_refresh(current_input_location, view_function)
            current_input_location = current_input_location + 1
        sql_handler.save_load(data_entered)
        display('view', data_entered[0])

    if view_function == 'view':
        data_entered = sql_handler.get_load_by_id(load_id)
        display_refresh(0, view_function)

    if view_function == 'new':
        data_entered[0] = now.strftime("%Y%m%d%H%M%S")
        current_input_location = 1
        while current_input_location < 24:
            display_refresh(current_input_location, view_function)
            current_input_location = current_input_location + 1
        sql_handler.save_load(data_entered)
        display('view', data_entered[0])


def current_location_text_getter(index):
    switcher = {
        0: "",
        1: " or LOAD NAME",
        2: " or CARTRIDGE NAME",
        3: " or COAL",
        4: " or VELOCITY",
        5: " or BRASS BRAND",
        6: " or TIMES BRASS WAS FIRED",
        7: " or LENGTH OF BRASS",
        8: " or BRASS TUMBLED (YES/NO)",
        9: " or BRASS ANNEALED (YES/NO)",
        10: " or BRASS TRIMMED (YES/NO)",
        11: " or BRASS CHAMFERED (YES/NO)",
        12: " or BRASS DEBURRED (YES/NO)",
        13: " or CRIMP TYPE",
        14: " or CRIMP OD",
        15: " or PRIMER BRAND",
        16: " or PRIMER MODEL",
        17: " or POWDER BRAND",
        18: " or POWDER MODEL",
        19: " or POWDER WEIGHT IN GRAINS",
        20: " or PROJECTILE BRAND",
        21: " or PROJECTILE MODEL",
        22: " or PROJECTILE WEIGHT IN GRAINS",
        23: " or NOTES",
    }
    return switcher.get(index, " ERROR")


def process_input(options_and_commands_list, current_input_location, view_function):
    global data_entered
    current_location_text = current_location_text_getter(current_input_location)
    menu_global_commands.display_load_command(options_and_commands_list, f'Command{current_location_text}:')
    user_input_command = menu_global_commands.input_loop()
    if user_input_command == 'q':
        sql_handler.close_and_save()
        quit()
    elif user_input_command == 'c' and view_function == 'new':
        menu_main.display()
    elif user_input_command == 'c' and view_function == 'edit':
        display('view', data_entered[0])
    elif user_input_command == 's' and view_function == 'edit':
        sql_handler.save_load(data_entered)
        display('view', data_entered[0])
    elif user_input_command == 's' and view_function == 'new':
        sql_handler.save_load(data_entered)
        display('view', data_entered[0])
    elif user_input_command == 'e' and view_function == 'view':
        display('edit', data_entered[0])
    elif user_input_command == 'b' and view_function == 'view':
        menu_select_load.display(data_entered[2])
    elif user_input_command == 'p' and view_function == 'view':
        pdf_handler_load_data.generate_load_pdf(data_entered)
        menu_global_commands.move_cursor_to_line()
        process_input(options_and_commands_list, current_input_location, view_function)
    elif user_input_command == 'l' and view_function == 'view':
        pdf_handler_load_data.generate_box_pdf(data_entered)
        menu_global_commands.move_cursor_to_line()
        process_input(options_and_commands_list, current_input_location, view_function)
    elif view_function == 'edit':
        data_entered[current_input_location] = user_input_command
    elif view_function == 'new':
        data_entered[current_input_location] = user_input_command
    else:
        menu_global_commands.move_cursor_to_line()
        process_input(options_and_commands_list, current_input_location, view_function)

