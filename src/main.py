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
            "blue": "\033[3m",
            "magenta": "\033[35m",
            "cyan": "\033[36m",
            "yellow": "\033[33m",
        },
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
    },
    "text-stlye": {
        "name": "Text Style",
        "items": {
            "bold": "\033[1m",
            "italic": "\033[3m",
            "underline": "\033[4m",
            "strikethrough": "\033[9m",
        },
    }
}


def push_screen(key = ""):
    # home screen
    if not key:
        print("│", "\033[1mMAIN MENU\033[0m", "\n│") # title
        for index, keys in enumerate(list(SCREEN_ITEMS.keys())):
            print(f"┝ {index + 1})", SCREEN_ITEMS[keys]["name"])
            time.sleep(0.1)

        print("│\n┝", "x) Done")
        print("└────────────────────────────┘")
        home_screen_navigation()

    # all color screens
    else:
        print("│\033[1m", SCREEN_ITEMS[key]["name"], "\033[0m\n│") # title
        for index, item in enumerate(list(SCREEN_ITEMS[key]["items"].items())):
            print(f"┝ {index + 1})", item[1] + "▆" + "\033[0m", item[0])
            time.sleep(0.1)

        print("│\n┝", "x) Back")
        print("└────────────────────────────┘")


def home_screen_navigation():
    while True:
        try:
            choice = int(input("> "))
        except ValueError:
            print("Please choose a valid number")
            continue
        break

    # move cursor to home -> move X lines down -> delete everything until end of screen
    print("\033[H" "\033[3E" "\033[0J", end="")
    push_screen(list(SCREEN_ITEMS.keys())[choice - 1])


# PROGRAM START

# Default styling
# print("\033[30;47m  ", end="")

# header
print("┌────────────────────────────┐")
print("│ \033[33;1mANSI Escape Code Generator\033[0m │")
print("├────────────────────────────┤")
time.sleep(0.1)

# home screen
push_screen()
home_screen_navigation()

