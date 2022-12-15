import os
import time

os.system("cls")


SCREEN_ITEMS = {
    "foreground-color": {
        "name": "Foreground Color",
        "items": {
            "white": "\033[37m",
            "black": "\033[30m",
            "red": "\033[31m",
            "green": "\033[32m",
            "blue": "\033[34m",
            "magenta": "\033[35m",
            "cyan": "\033[36m",
            "yellow": "\033[33m",
        },
        "selected": ""
    },
    "background-color": {
        "name": "Background Color",
        "items": {
            "white": "\033[47m",
            "black": "\033[40m",
            "red": "\033[41m",
            "green": "\033[42m",
            "blue": "\033[44m",
            "magenta": "\033[45m",
            "cyan": "\033[46m",
            "yellow": "\033[43m",
        },
        "selected": ""
    },
    "text-stlye": {
        "name": "Text Style",
        "items": {
            "bold": "\033[1m",
            "italic": "\033[3m",
            "underline": "\033[4m",
            "strikethrough": "\033[9m",
        },
        "selected": ""
    }
}


def print_selection(current_screen):
    selection = SCREEN_ITEMS[current_screen]["selected"]
    if selection:
        print(SCREEN_ITEMS[current_screen]["items"][selection], selection, "\033[0m")
    else:
        print() # we need a linebreak


def push_screen(key = ""):
    # move cursor to home -> 
    # move cursor few lines down to keep header -> 
    # delete everything until end of screen
    print("\033[H" "\033[3E" "\033[0J", end="")

    # home screen
    if not key:
        print("│", "\033[1mMAIN MENU\033[0m", "\n│") # title
        for index, keys in enumerate(list(SCREEN_ITEMS.keys())):
            print(f"┝ {index + 1})", SCREEN_ITEMS[keys]["name"], end="")
            print_selection(keys)
            time.sleep(0.1)


        print("│\n┝", "0) Done")
        print("└────────────────────────────")
        handle_navigation("home")

    # all other screens
    else:
        print("│\033[1m", SCREEN_ITEMS[key]["name"], "\033[0m\n│") # title
        for index, item in enumerate(list(SCREEN_ITEMS[key]["items"].items())):
            print(f"┝ {index + 1})", item[1] + "▆" + "\033[0m", item[0])
            time.sleep(0.05)

        print("│\n┝", "0) Back")
        print("└────────────────────────────")
        handle_navigation(key)


def handle_navigation(current_screen):
    while True:
        try:
            choice = int(input("> "))

            if current_screen == "home":
                keys = list(SCREEN_ITEMS.keys())
                if not choice - 1 in range(len(keys)):
                    raise ValueError
                push_screen(keys[choice - 1])

            else:
                if choice == 0:
                    push_screen() # home screen
                
                keys = list(SCREEN_ITEMS[current_screen]["items"].keys())
                if not choice - 1 in range(len(keys)):
                    raise ValueError
                
                print(SCREEN_ITEMS[current_screen]["name"] + ":", keys[choice - 1], "selected")
                SCREEN_ITEMS[current_screen]["selected"] = keys[choice - 1]
                time.sleep(1)
                push_screen()

        except ValueError:
            print("Please choose a valid option")
            continue
        
        break



# PROGRAM START

# Default styling
# print("\033[30;47m  ", end="")

# header
print("┌────────────────────────────┐")
print("│ \033[33;1mANSI Escape Code Generator\033[0m │")
print("├────────────────────────────┘")
time.sleep(0.1)

# home screen
push_screen()
