import main as main
import os
import shutil
import sys
from colorama import Fore, Style


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def generate_horizontal_line():
    line_builder = 0
    horizontal_line = ''
    while line_builder <= 115:
        horizontal_line = horizontal_line + '̅'
        line_builder = line_builder + 1
    return horizontal_line


def display_options_and_commands(options_and_commands_list):
    print(Fore.GREEN + "\n\n\n  Selection or command:")
    print(Fore.GREEN + "  ===> \n  " + generate_horizontal_line())
    command_string = "\n  " + Fore.BLUE
    for item in options_and_commands_list:
        if item == 'q':
            command_string = command_string + 'q =Quit Program     '
        if item == 'b':
            command_string = command_string + 'b =Go Back     '
        if item == 'e':
            command_string = command_string + 'e =Edit     '
        if item == 'c':
            command_string = command_string + 'c =Cancel     '
        if item == 's':
            command_string = command_string + 's =Save     '
        if item == 's':
            command_string = command_string + 'd =Delete     '
        if item == 'p':
            command_string = command_string + 'p =Print Load Data     '
        if item == 'l':
            command_string = command_string + 'l = Print Box Label     '
    print(command_string)
    sys.stdout.write('\x1b[3A')


def display_load_command(options_and_commands_list, instructions):
    print(Fore.GREEN + f"\n  {instructions}")
    print(Fore.GREEN + "  ===> \n  " + generate_horizontal_line())
    command_string = "\n  " + Fore.BLUE
    for item in options_and_commands_list:
        if item == 'q':
            command_string = command_string + 'q =Quit Program     '
        if item == 'b':
            command_string = command_string + 'b =Go Back     '
        if item == 'e':
            command_string = command_string + 'e =Edit     '
        if item == 'c':
            command_string = command_string + 'c =Cancel     '
        if item == 's':
            command_string = command_string + 's =Save     '
        if item == 's':
            command_string = command_string + 'd =Delete     '
        if item == 'p':
            command_string = command_string + 'p =Print Load Data     '
        if item == 'l':
            command_string = command_string + 'l = Print Box Label     '
    print(command_string)
    move_cursor_to_line()


def move_cursor_to_line():
    sys.stdout.write('\x1b[3A')


def input_loop():
    sys.stdout.write('\x1b[1A')
    print(f"{Fore.BLUE}  ===>                                                                                        ")
    sys.stdout.write('\x1b[1A')
    print(f"{Fore.BLUE}  ===>  {Fore.WHITE}", end='')
    return input()


def display_prompt(prompt):
    print(" " + Fore.BLUE + prompt + Style.RESET_ALL)


def display_title(page):
    remove_characters = len(page) * 2 + 2
    print("\n " + Fore.BLUE + page + Fore.WHITE +
          f"Reloading Journal {main.version}".center(shutil.get_terminal_size().columns - remove_characters) +
          Style.RESET_ALL)


def display_list(list_items):
    for idx, item in enumerate(list_items):
        position = idx + 1
        print("\t" + Fore.WHITE + "{0: =2d}. ".format(position) + Fore.GREEN + item + Style.RESET_ALL)
    padding = 18 - len(list_items)
    if padding == 18:
        padding = padding - 1
        print("\tNo results Found")
    while padding >= 0:
        padding = padding - 1
        print("\t")


def index_counter(passed_list):
    index_list = []
    for idx, item in enumerate(passed_list):
        index_list = index_list + [f"{idx + 1}"]
    return index_list
