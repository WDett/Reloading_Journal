import menus.menu_global_commands as menu_global_commands
import sql_handler.sql_handler as sql_handler
import menus.menu_nev_load as menu_nev_load
import menus.menu_select_cartridge as menu_select_cartridge


def display(selected_cartridge):
    option_list, load_id_list = sql_handler.get_recipes_by_cartridges(selected_cartridge)

    option_list_index = menu_global_commands.index_counter(option_list)
    command_list = ['q', 'b']
    options_and_commands_list = option_list_index + command_list
    user_input_command = ""
    while user_input_command not in options_and_commands_list:
        menu_global_commands.clear_console()
        menu_global_commands.display_title("SELECT LOAD")
        menu_global_commands.display_prompt("\n\n  Select one of the following:\n")
        menu_global_commands.display_list(option_list)
        menu_global_commands.display_options_and_commands(options_and_commands_list)
        user_input_command = menu_global_commands.input_loop()
    if user_input_command == 'q':
        sql_handler.close_and_save()
        quit()
    if user_input_command == 'b':
        menu_select_cartridge.display()
    elif int(user_input_command) <= len(option_list) and not 0:
        menu_nev_load.display('view', load_id_list[int(user_input_command) - 1][0])
