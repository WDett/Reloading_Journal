import menus.menu_global_commands as menu_global_commands
import menus.menu_select_cartridge as menu_select_cartridge
import menus.menu_nev_load as menu_nev_load
import sql_handler.sql_handler as sql_handler


def display():
    option_list = ['Create new load', 'View list of existing loads']
    option_list_index = menu_global_commands.index_counter(option_list)
    command_list = ['q']
    options_and_commands_list = option_list_index + command_list
    user_input_command = ""
    while user_input_command not in options_and_commands_list:
        menu_global_commands.clear_console()
        menu_global_commands.display_title("MAIN")
        menu_global_commands.display_prompt("\n\n  Select one of the following:\n")
        menu_global_commands.display_list(option_list)
        menu_global_commands.display_options_and_commands(options_and_commands_list)
        user_input_command = menu_global_commands.input_loop()
    if user_input_command == 'q':
        sql_handler.close_and_save()
        quit()
    elif user_input_command == '1':
        menu_nev_load.display('new', '0')
    elif user_input_command == '2':
        menu_select_cartridge.display()
